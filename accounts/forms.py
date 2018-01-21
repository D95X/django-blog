from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=20,
                            widget=forms.TextInput(attrs={'class' :'form-control', 'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
								attrs={'class' :'form-control', 'placeholder' : 'password'}))


class SignupForm(forms.Form):
    username = forms.EmailField(max_length=20,
                            widget=forms.TextInput(attrs={'class' :'form-control', 'placeholder' : 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
								attrs={'class' :'form-control', 'placeholder' : 'password'}))

    password2 = forms.CharField( widget=forms.PasswordInput(
                                 attrs={'class': 'form-control', 'placeholder': 'r_password'} ) )