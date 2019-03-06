from django import forms
# from django.contrib.auth.models import User

from tourx.models import Profile


class ProfileForm(forms.ModelForm):
    retype_pass = forms.PasswordInput(attrs={'placeholder': 'Retype Password'})

    class Meta:
        model = Profile
        fields = (
        'email', 'password', 'first_name', 'last_name', 'mobile', 'address', 'profile_pic', 'photo_id', 'birth')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            # 'profile_pic': forms.ImageField(),
            # 'photo_id': forms.ImageField(),
            'birth': forms.SelectDateWidget(),
        }
