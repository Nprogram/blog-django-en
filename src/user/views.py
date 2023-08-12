from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfilUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            #username = form.cleaned_data['username']
            messages.success(request, 'felecitation! {} inscription validée.'.format(new_user) )
            #messages.success(request, f'felecitation! {username} inscription validée.')
            return redirect('login')
        # else:
        #     messages.error(request, "Invalide nom d'utilisateur ou mot de passe!.")
    else:
        form = UserCreationForm()
    
    return render(request,'user/register.html', {
        'title': 'Inscription',
        'form': form,
        } )

def login_user(request):
    if request.method == 'POST':
        # form = LoginForm
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie")
            
            return redirect('profile')
        # else:
        #     messages.warning(request, "Nom d'utilisateur incorrect!")

    # else:
    #     form = LoginForm

    return render(request, 'user/login.html', {
        'title' : 'Connexion',
        # 'form' : form,
    })
def logout_user(request):
    logout(request)
    # messages.success(request, "Deconnexion réussie à bientot!")
    return render (request, 'user/logout.html',{
        'title' : 'Deconnexion..',
    })
@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render (request, 'user/profile.html',{
        'title' : 'Profile personnel',
        'posts' : posts,
        'page' : page,
        'post_list': post_list,

    })
@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile modifier.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'title' : 'Modifier profile',
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request, 'user/profile_update.html', context)