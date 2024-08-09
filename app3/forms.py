from django import forms
class SignupForm(forms.Form):
    username=forms.CharField(label="username",max_length=200)
    email=forms.EmailField(label="email",max_length=200)
    password=forms.CharField(widget=forms.PasswordInput,label="password",max_length=200)
    password_confirm=forms.CharField(widget=forms.PasswordInput,label='password_confirm',max_length=200)

