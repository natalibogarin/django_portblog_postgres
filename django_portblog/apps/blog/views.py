from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)


# Create your views here.
def blog_index(request):
    post_list = Post.objects.all().order_by('-created_on')
    context = {
        "posts": post_list,
    }
    return render(request, "blog_index.html", context)


def blog_detail(request, id):
    try:
        data =Post.objects.get(id =id)
        comments = Comment.objects.filter(approved_comment=True)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')

    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.isvalid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["author"])
            print("Comentario:" + form.cleaned_data["comment_body"])
            comment = Comment(
                author=form.cleaned_data["author"],
                comment_body=form.cleaned_data["comment_body"],
                post=data
            )
            comment.save()

    comments = Comment.objects.filter(approved_comment=True)
    context = {
        "post": data,
        "comments": comments,
        "form": form,
    }

    return render(request, 'post_detail.html', context)


class CreatePostView(CreateView, LoginRequiredMixin):
    login_url= '/login'
    #redirect_field_name='index_detail.html'

    form_class = PostForm

    model = Post


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


@login_required
def post_publish(request, id):
    try:
        post =Post.objects.get(id =id)
    except Post.DoesNotExist:
        raise Http404('Data does not exist')
    post.publish()
    return redirect('post_detail', id=id)


@login_required
def comment_approve(request, id):
    try:
        comment =Comment.objects.get(id =id)
    except Comment.DoesNotExist:
        raise Http404('Comentario no existe')
    comment.approve()
    return redirect('post_detail', id=comment.post.id)


@login_required
def comment_remove(request, id):
    try:
        comment =Comment.objects.get(id =id)
    except Comment.DoesNotExist:
        raise Http404('Comentario no existe')
    post_id = comment.post.id
    comment.delete()
    return redirect('post_detail', id=post_id)


def contact(request):
    #return HttpResponse("Hola estoy en la pagina de contacto")
    return render(request, 'index copy.html',{})