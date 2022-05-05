from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)