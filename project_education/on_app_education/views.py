

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

# تسجيل حساب جديد
def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # يسجل دخوله مباشرة
            return redirect("dashboard")
    else:
        form = SignUpForm()
    return render(request, "on_app_education/register.html", {"form": form})

# تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "on_app_education/login.html", {"form": form})

# تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect("login")

# الصفحة الرئيسية بعد تسجيل الدخول
@login_required
def dashboard(request):
    return render(request, "on_app_education/*dashboard.html", {"user": request.user})
