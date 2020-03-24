from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})
    # methoud request and return the model for render , where mont the model  html

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == 'POST': #if form contain value
        form = PostForm(request.POST)

        if(form.is_valid()):#form correct with values corrects
            post = form.save(commit = False)#not save post model yet
            post.author = request.user#first add author in request.user
           # post.published_date = timezone.now()# time and date now 
            post.save() #save post with changes
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()#return view when finish with dates 
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})   

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)           
      