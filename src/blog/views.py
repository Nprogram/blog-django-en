from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import NewComment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
# posts = [
#     {
# 'title': 'Premièr blog',
#     'content': 'text première blog comme test',
#     'post_date':'15-3-2019',
#     'author' : 'Oussama Kadi'
# },
#  {
# 'title': 'Dexième blog',
#     'content': 'text dexième blog comme test',
#     'post_date':'25-3-2019',
#     'author' : 'Imen telli'
# },
#  {
# 'title': 'Troisième blog',
#     'content': 'text troisième blog comme test',
#     'post_date':'20-3-2019',
#     'author' : 'Kamel Khadi'
# },
#  {
# 'title': 'Quatrième blog',
#     'content': 'text quatrième blog comme test',
#     'post_date':'30-3-2019',
#     'author' : 'Fatehia Dahou'
# }
    
# ]



def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title' : 'Page principale',
        'posts' : posts,
        'page' : page,

    }
    return render(request, 'blog/index.html', context)

def about(request):
   
    return render(request, 'blog/about.html',{'title':'About me !'})

def post_detail(request, post_id):
    post= get_object_or_404(Post, pk=post_id)
    comments= post.comments.filter(active=True)
    # comment_form = NewComment()
    # new_comment = None
    if request.method == "POST":
        comment_form= NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form= NewComment()
    else:
        comment_form = NewComment()
    context = {
        'title': post,
        'post' : post,
        'comments' : comments,
        'comment_form': comment_form,
    }
    
    return render(request,'blog/detail.html',context)

    