from django.shortcuts import render
from django.views import View 
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import User, Shop, Item, Inventory
from django.urls import reverse

class Home(TemplateView):
    template_name='home.html'
    
    def login_page(request):
        context = {
            'login': login,
        }
    
        return render(request, context)
    
    
#SHOP VIEWS
class Shop_Create(CreateView):
  model = Shop
  fields = '__all__'
  template_name='shop_create.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/shop/')



class Shop_List(TemplateView):
    template_name = "shop_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
                # to get the query parameter we have to acccess it in the request.GET dictionary object  
        # If a query exists we will filter by name       
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param

            context["shops"] = Shop.objects.filter(name__icontains=name)
            context["header"] = f'Searching for {name}'
        else: 
            context["shops"] = Shop.objects.all() # this is where we add the key into our context object for the view to use
            context["header"] = "Our Cats:"
        return context

    
   
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


def Shop_Show(request, device_id):
    shops = Shop.objects.get(id=device_id)
    return render(request, 'shop_show.html', {'shops': shops})