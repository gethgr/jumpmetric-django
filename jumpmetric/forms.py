from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Trial

class UserRegisterForm(UserCreationForm):  
    fullname = forms.CharField(max_length = 50)
    occupy = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User 
        fields = ['username', 'email',  'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class prepare_new_trial_Form(forms.Form):
    #name = forms.CharField(max_length=100)
    prepare_file = forms.FileField()
    

#create a ModelForm
class insert_new_trial_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Trial
       
        fields = "__all__"
        #fields =['fullname','height','weight','age','email','occupy','type_of_trial','drop_jump_height','trial_csv',]