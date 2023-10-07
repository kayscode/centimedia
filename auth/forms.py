from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.TextInput)


class LogoutForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)