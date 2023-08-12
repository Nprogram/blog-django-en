from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, help_text="Le nom d'utilisateur ne doit pas contenir des espaces!")
    email = forms.EmailField()
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='confirmation mot de passe', widget=forms.PasswordInput(), min_length=8)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                   'last_name', 'password1', 'password2')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('mot de passe non conformes!')
        return cd['password2']
    
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username = cd['username']).exists():
            raise forms.ValidationError('Nom utilisateur existe déja!')
        return cd['username']
    
class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')
# class LogoutForm(forms.ModelForm):
#     username = forms.CharField(label="Nom d'utilisateur")
#     password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ('username', 'password')

class UserUpdateForm(forms.ModelForm):
    
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')  
class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)    
