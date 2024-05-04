from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def start_view(request):
    return render(request, 'index.html')
