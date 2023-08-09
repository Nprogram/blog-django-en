from django.shortcuts import render
from .forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'Inscription',
        'form': form,
    } )