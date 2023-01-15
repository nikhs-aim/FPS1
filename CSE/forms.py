from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    dept_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())

    GENDER=(('Male','Male'),('Female','Female'))
    gender=forms.ChoiceField(choices=GENDER)

    ROLE=(('HOD','HOD'),('OTHER','OTHER'))
    role=forms.ChoiceField(choices=ROLE)

    
    class Meta:
        model = User
        fields = ['username', 'email','role','dept_name','age','gender', 'password1', 'password2']