from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')


def him(request):
    another_page_url = '/another_page/'
    return render(request, 'kunu.html', {'another_page_url': another_page_url})