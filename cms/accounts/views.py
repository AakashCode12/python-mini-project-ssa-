
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
import collections


def index(request):
    return render(request, 'index.html')
