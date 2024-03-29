from django import forms
from django.contrib.auth.forms import UserCreationForm
from requests import request
from .models import *










#Application forms
class Registration(UserCreationForm):
  email = forms.EmailField(max_length=60, label='Email', help_text='Required. Add a valid email address. Used to log in.')
  first_name = forms.CharField(label='Name')
  password1 = forms.CharField(label='Create password', widget=forms.PasswordInput())
  def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        for fieldname in ['email','password1', 'password2']:
            self.fields[fieldname].help_text = None
  class Meta: 
    model = NewUser
    fields = ['email', 'first_name', 'password1', 'password2']





class Audioform(forms.ModelForm):
    title = forms.CharField(label='Title')
    audio = forms.FileField(label='', widget=forms.FileInput(attrs={'id':'myfiles', 'class':'text-xl w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none hidden', 'onchange':'pullfiles' }))
    
    class Meta:
        model = Audio
        fields = ('audio', 'title')