from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, SignUpForm
from .models import Post


# ഹോംപേജ് കാണിക്കാനുള്ള വ്യൂ
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/home.html", {"posts": posts})


# സിംഗിൾ പോസ്റ്റ് വ്യൂ
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/detail.html", {"post": post})


# പുതിയ പോസ്റ്റ് ഉണ്ടാക്കാനുള്ള വ്യൂ (ലോഗിൻ ചെയ്തവർക്ക് മാത്രം)
@login_required(login_url="login")
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


# പോസ്റ്റ് എഡിറ്റ് ചെയ്യാനുള്ള വ്യൂ (ലോഗിൻ ചെയ്തവർക്ക് മാത്രം)
@login_required(login_url="login")
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})


# പോസ്റ്റ് ഡിലീറ്റ് ചെയ്യാനുള്ള വ്യൂ (ലോഗിൻ ചെയ്തവർക്ക് മാത്രം)
@login_required(login_url="login")
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "blog/post_confirm_delete.html", {"post": post})


# പുതിയ യൂസർ രജിസ്ട്രേഷൻ
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "blog/signup.html", {"form": form})


# യൂസർ ലോഗിൻ
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


# യൂസർ ലോഗൗട്ട്
def logout_view(request):
    logout(request)
    return redirect("home")