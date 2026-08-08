from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# إنشاء حساب جديد
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="البريد الإلكتروني")
    first_name = forms.CharField(max_length=30, required=False, label="الاسم الأول")
    last_name = forms.CharField(max_length=30, required=False, label="الاسم الأخير")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

# تسجيل الدخول
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="اسم المستخدم")
    password = forms.CharField(widget=forms.PasswordInput, label="كلمة المرور")