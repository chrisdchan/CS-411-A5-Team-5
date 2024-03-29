
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import os
from django.db.models import Q
import openai
from dotenv import load_dotenv
from django.views.generic.edit import DeleteView
load_dotenv()


ASSEMBLY_KEY = os.getenv("ASSEMBLY_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")


# Main View
def index(request):
    context = {}

    if request.user.is_authenticated:
        #redirect to dashboard if user is logged in
        return redirect('dashboard')

    return render(request, 'index.html', context)


def get_context(request, searchTerm):
    context = {}

    context['searchTerm'] = searchTerm
    context['audiologs'] = []
    headers = {
        "authorization": f"{ASSEMBLY_KEY}",
    }

    #Getting all user's meetings
    audiologs = Audio.objects.filter(supervisor=request.user)

    #If a search term is provided, filter the meetings
    if searchTerm != None:
        audiologs = audiologs.filter(
            Q(transcription__icontains=searchTerm) | Q(summary__icontains=searchTerm) | Q(title__icontains=searchTerm))

    #Checking the status of the meetings and processing them
    for audio in audiologs:
        endpoint = "https://api.assemblyai.com/v2/transcript/" + \
            str(audio.audioid)
        response = requests.get(endpoint, headers=headers)
        if response.json()['status'] == 'completed' and not audio.transcription:
            context['audiologs'] += [[audio, 1]]
            headers = {
                "authorization": f"{ASSEMBLY_KEY}",
            }
            endpoint = "https://api.assemblyai.com/v2/transcript/" + \
                str(audio.audioid)
            response = requests.get(endpoint, headers=headers)
            audio.transcription = response.json()['text']
            audio.save()

            api_key = OPENAI_KEY

            endpoint = "https://api.openai.com/v1/completions"
            prompt = f"Summarize the following audio transcription: \n {audio.transcription}"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }

            data = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "max_tokens": 50,
                "n": 1,
                "stop": None,
                "temperature": 0.5
            }

            response = requests.post(endpoint, headers=headers, json=data)
            response_json = response.json()

            if response.status_code == 200:
                generated_text = response_json["choices"][0]["text"].strip()
                audio.summary = generated_text
                audio.save()
            else:
                print(f"Error: {response_json['error']['message']}")

        elif response.json()['status'] == 'completed' and audio.transcription:
            context['audiologs'] += [[audio, 1]]

        else:
            context['audiologs'] += [[audio, 0]]

    context['audiologs'] = context['audiologs'][::-1]
    return context

#Dashboard with context passed from index
@login_required
def dashboard(request):
    context = get_context(request, None)
    return render(request, 'dashboard.html', context)

#Filter for keyword search
@login_required
def filter(request):
    if request.method == 'POST':
        search = request.POST.get("search")
        if search == "":
            search = None
        context = get_context(request, search)
    else:
        context = get_context(request, None)

    return render(request, 'dashboard.html', context)

#Login view.
class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

#Signup view
class RegisterPage(FormView):
    redirect_authenticated_user = True
    template_name = 'account/signup.html'
    form_class = Registration

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')

#Audio upload view
class AudioCreate(LoginRequiredMixin, CreateView):
    form_class = Audioform
    template_name = 'audioform.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.supervisor = self.request.user
        return super(AudioCreate, self).form_valid(form)

#Meeting detail view
class AudioDetail(DetailView):
    model = Audio
    template_name = 'audiodetail.html'

#View to delete a meeting
class AudioDelete(DeleteView):
    model = Audio
    success_url = reverse_lazy('dashboard')

#API queryset
class UserViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer

#API queryset
class NestedViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NestedSerializer
