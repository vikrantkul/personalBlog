from django.shortcuts import render,redirect
from django.contrib.auth.models	import	User
from django.views import generic
from .forms import Post, CommentForm
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Post, Comment
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def PostList(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

#class PostList(generic.ListView):
 #   queryset = Post.objects.filter(status=1).order_by('-created')
  #  template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail.html', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail.html', pk=comment.post.pk)