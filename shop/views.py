from django.shortcuts import render
from django.views import View 
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from models import User, Shop, Item, Inventory
from django.urls import reverse

class Home(TemplateView):
    template_name='home.html'
    
    def login_page(request):
        context = {
            'login': login,
        }
    
        return render(request, context)
    
    
#SHOP VIEWS
class ShopCreate(CreateView):
  model = Shop
  fields = '__all__'
  template_name='shop_create.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/shops/new')



class Shop_List(TemplateView):
    template_name='shop_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
    

        if name != None:
                    context['shop']=Shop.objects.filter(name__icontains=name)
                    context['header']= f'Searching for {name}'
        else:
                    context['shops']=Shop.objects.all()
                    context['items']=Item.objects.all()
            
        context['header']= 'Shops:'
            
        return 
    
   
class Shop_Detail(DetailView):
    model = Shop
    template_name = "shop_detail.html"
    

class Shop_Update(UpdateView):
    model = Shop
    fields = '__all__'
    template_name = "shop_update.html"
    def get_success_url(self):
        return reverse('shop_detail', kwargs={'pk': self.object.pk})

class Shop_Delete(DeleteView):
    model = Shop
    template_name = 'shop_delete.html'
    success_url = "/shop/"
