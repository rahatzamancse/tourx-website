from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), max_length=100, label='Password')
    # profile_pic = forms.FileField(max_length=100, label='Profile Picture')
    mobile = forms.CharField(max_length=100, label='Mobile', widget=forms.TextInput(attrs={'placeholder': 'Mobile'}))
    # photo_id = forms.FileField(max_length=100, label='Photo ID')
    # is_scout = forms.BooleanField(label='Scout')
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    address = forms.CharField(max_length=200, label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(max_length=100, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'mobile', 'address']
