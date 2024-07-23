from django import forms
from django.contrib.auth.models import User
from .models import Profile, Song, Playlist

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model  = User
        fields = ['username', 'email', 'password']
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['picture', 'bio']
        
class PlaylistForm(forms.ModelForm):
    class Meta:
        model  = Playlist
        fields = ['name', 'songs']
        widgets = {
            'songs' : forms.CheckboxSelectMultiple(),
        }


        