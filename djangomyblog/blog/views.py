from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .models import Post, Comment
from .forms import CommentForm, CustomUserCreationForm


def home(request):
    posts = (
        Post.objects
        .filter(status='ON')
        .select_related('user')
        .order_by('-created_at')
    )
    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")


@login_required
def profile(request):
    return render(request, "blog/profile.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(
                request,
                "Este nome de usuário já existe. Escolha outro."
            )

    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status='ON')

    comments = (
        Comment.objects
        .filter(post=post, status='ON')
        .select_related('user')
        .order_by('-created_at')
    )

    form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("post_detail", id=post.id)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        }
    )


@login_required
def new_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                user=request.user,
                status='ON'
            )
            return redirect("home")

    return render(request, "blog/new_post.html")


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, status='ON')

    if post.user != request.user:
        return redirect("home")

    post.status = 'DEL'
    post.save(update_fields=['status'])

    return redirect("home")
