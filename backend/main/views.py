
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
import openai
from dotenv import load_dotenv
from django.views.generic.edit import DeleteView
load_dotenv()


ASSEMBLY_KEY = os.getenv("ASSEMBLY_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")


def index(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'index.html', context)


@login_required
def dashboard(request):
    context = {}

    context['audiologs'] = []
    headers = {
        "authorization": f"{ASSEMBLY_KEY}",
    }
    audiologs = Audio.objects.filter(supervisor=request.user)
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

    return render(request, 'dashboard.html', context)


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


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

class AudioCreate(LoginRequiredMixin, CreateView):
    form_class = Audioform
    template_name = 'audioform.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.supervisor = self.request.user
        return super(AudioCreate, self).form_valid(form)


class AudioDetail(DetailView):
    model = Audio
    template_name = 'audiodetail.html'

class AudioDelete(DeleteView):
    model = Audio
    success_url = reverse_lazy('dashboard')




class UserViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer


class NestedViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NestedSerializer
