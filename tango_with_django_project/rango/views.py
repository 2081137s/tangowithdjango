from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('''Rango says hey there world!
<br/> <a href='/rango/about'>About</a>''')

def about(request):
    return HttpResponse('''Rango says here is the about page.
<br/> This tutorial has been put together by Thomas Shearer, 2081137s <br/>
<a href="/rango/">Index</a>''')
