from django import forms
from cProfile import label

class LoginFrom(forms.Form):
    Username=forms.CharField(label=' User ',max_length=20)
    Password=forms.CharField(label="Pwd",widget=forms.PasswordInput)
class SignForm(forms.Form):
    Usename=forms.CharField(max_length=20)
    Password=forms.CharField(widget=forms.PasswordInput)
    Email=forms.EmailField(widget=forms.EmailInput)
    Signature=forms.CharField(widget=forms.Textarea)