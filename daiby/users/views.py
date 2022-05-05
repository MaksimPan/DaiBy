from django.shortcuts import render
from django.http import HttpResponse

def profiles(request):
    return render(request, 'users/profiles.html')

def profile(request, pk):
    return render(request, 'users/profile.html')