from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'felecitation! {} inscription validée.'.format(username) )
            #messages.success(request, f'felecitation! {username} inscription validée.')
            return redirect('home')
        else:
            messages.error(request, "Invalide nom d'utilisateur ou mot de passe!.")
    else:
        form = UserCreationForm()
    
    return render(request,'user/register.html', {
        'title': 'Inscription',
        'form': form,
        } )

def login_user(request):
    if request.method == 'POST':
        form = LoginForm
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie")
            return redirect('home')
        else:
            messages.warning(request, "Nom d'utilisateur incorrect!")

    else:
        form = LoginForm

    return render(request, 'user/login.html', {
        'title' : 'Connexion',
        'form' : form,
    })
def logout_user(request):
    logout(request)
    messages.success(request, "Deconnexion réussie à bientot!")
    return render (request, 'user/logout.html',{
        'title' : 'Deconnexion..',
    })
