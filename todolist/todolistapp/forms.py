from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from todolistapp.models import TodoListModel


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'password'}))
    
    class Meta:
        model = User
        fields = ['username', 'password']
        

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border-b-2 border-b-blue-500', 'placeholder': 'Password again'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class AddTodoItemForm(forms.Form):
    class Meta:
        model = TodoListModel
        fields = ['text']