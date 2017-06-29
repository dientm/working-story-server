from django import forms

class AvatarUploadForm(forms.Form):
    username = forms.CharField()
    avatar = forms.ImageField()