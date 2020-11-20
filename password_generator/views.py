from django.shortcuts import render
from django.http import request
import random
# Create your views here.
def home(request):
  return render(request,'home.html')
def password(request):

  characters=list('abcdefghijklmnopqrstuvwxyz')
  if request.GET.get('uppercase'):
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
  if request.GET.get('special'):
    characters.extend(list('`=-~!@#$%^&*()_+'))
  if request.GET.get('number'):
    characters.extend(list('1234567890'))

  length = int(request.GET.get('length'))

  thepass=''
  for x in range(length):
    thepass +=random.choice(characters)
  return render(request,'password.html',{'password':thepass})

def about(request):
  return render(request,'about.html')