from django import forms

class PostForm(forms.Form):
    your_answer = forms.CharField(label='Your answer', max_length=500)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=200)

class UserCreationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=200)
   




