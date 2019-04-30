from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question
from django.utils import timezone

def home(request):
    return render(request, 'qa/home.html',{})