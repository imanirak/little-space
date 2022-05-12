from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
# Create your views here.



class Home(TemplateView):
    template_name='home.html'
    
    def login_page(request):
        context = {
            'login': login,
        }
    
        return render(request, context)
    
    
