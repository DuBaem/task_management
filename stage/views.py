from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def home(request):
    return render(request, 'stage/index.html')

def signup(request):
    return render(request, 'stage/signUp.html')
