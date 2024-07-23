from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, PlaylistForm
from .models import Profile, Playlist, Song, User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html',{'songs':songs})

def logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user= user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request,'register.html',{'form' : form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form,})

@login_required   
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form' : form, 'profile_form':profile_form})

@login_required  
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()
            return redirect('playlists')
    else:
        form = PlaylistForm()
    return render(request, 'playlist_form.html', {'form' : form,})

@login_required
def delete_playlist(request,playlist_id):
    playlist = get_object_or_404(Playlist, id = playlist_id)
    if request.method == 'POST':
        playlist.delete()
        return redirect('playlists')
    return render(request, 'playlist_confirm_delete.html', {'playlist' : playlist})

@login_required
def playlists(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlists.html', {'playlists':playlists})

@login_required
def update_playlist(request,playlist_id):
    playlist = get_object_or_404(Playlist, id = playlist_id)
    if request.method == 'POST':
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            playlist = form.save()
            return redirect('playlists')
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'playlist_form.html', {'form' : form,})


def search(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)
        songs = Song.objects.filter(title__icontains=query)
        playlists = Playlist.objects.filter(name__icontains=query)
    else:
        users = User.objects.none()
        songs = Song.objects.none()
        playlists = Playlist.objects.none()
    return render(request, 'search.html', {'users':users, 'songs':songs, 'playlists': playlists})
    
        