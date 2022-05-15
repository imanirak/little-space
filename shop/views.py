
from .models import User, Shop, Item, Inventory
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.db.models import F
from django.forms import Select
from .forms import ShopForm, ItemForm

###########################SIGNUP##################################

@login_required
def profile(request, username):
    owner = User.objects.get(username=username)
    shops = Shop.objects.filter(owner=owner.id)
    items = Item.objects.all()
    inventory = Inventory.objects.all()

    return render(request, 'profile.html', {'username': username, 'shops': shops, 'inventory':inventory, 'items': items, 'owner':owner})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request,'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    

class Home(TemplateView):
    shops = Shop.objects.all()
    template_name='home.html'
    
    def login_page(request):
        context = {
            'login': login,
        }
    
        return render(request, context)
    
    
#SHOP VIEWS

@method_decorator(login_required, name="dispatch")
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
    
    

@method_decorator(login_required, name="dispatch")
class Shop_Update(UpdateView):
    model = Shop
    fields = '__all__'
    template_name = "shop_update.html"
    def get_success_url(self):
        return reverse('shop_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name="dispatch")
class Shop_Delete(DeleteView):
    model = Shop
    template_name = 'shop_delete.html'
    success_url = "/shop/"


def Shop_Show(request, shop_id):
    shops = Shop.objects.get(id=shop_id)
    return render(request, 'shop_show.html', {'shops': shops})




#INVENTORY VIEWS

@method_decorator(login_required, name="dispatch")
class Inventory_Create(CreateView):
  model = Inventory
  fields = '__all__'
  template_name='inventory_create.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/inventory/')



@method_decorator(login_required, name="dispatch")
class Inventory_List(TemplateView):
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
                # to get the query parameter we have to acccess it in the request.GET dictionary object  
        # If a query exists we will filter by name       
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param

            context["inventorys"] = Inventory.objects.filter(name__icontains=name)
            context["header"] = f'Searching for {name}'
        else: 
            context["inventorys"] = Inventory.objects.all() # this is where we add the key into our context object for the view to use
            context["header"] = "Inventory:"
        return context

    
 
@method_decorator(login_required, name="dispatch")  
class Inventory_Detail(DetailView):
    model = Inventory
    template_name = "inventory_detail.html"
    

@method_decorator(login_required, name="dispatch")
class Inventory_Update(UpdateView):
    model = Inventory
    fields = '__all__'
    template_name = "inventory_update.html"
    def get_success_url(self):
        return reverse('inventory_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name="dispatch")
class Inventory_Delete(DeleteView):
    model = Inventory
    template_name = 'inventory_delete.html'
    success_url = "/inventory/"


def Inventory_Show(request, inventory_id):
    inventorys = Inventory.objects.get(id=inventory_id)
    return render(request, 'inventory_show.html', {'inventorys': inventorys})





#ITEM VIEWS

@method_decorator(login_required, name="dispatch")
class Item_Create(CreateView):
  model = Item
  fields = '__all__'
  template_name='item_create.html'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/item/')



@method_decorator(login_required, name="dispatch")
class Item_List(TemplateView):
    template_name = "item_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
                # to get the query parameter we have to acccess it in the request.GET dictionary object  
        # If a query exists we will filter by name       
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param

            context["items"] = Item.objects.filter(name__icontains=name)
            context["header"] = f'Searching for {name}'
        else: 
            context["items"] = Item.objects.all() # this is where we add the key into our context object for the view to use
            context["header"] = "Items:"
        return context

    

@method_decorator(login_required, name="dispatch")
class Item_Detail(DetailView):
    model = Item
    template_name = "item_detail.html"
    

@method_decorator(login_required, name="dispatch")
class Item_Update(UpdateView):
    model = Item
    fields = '__all__'
    template_name = "item_update.html"
    def get_success_url(self):
        return reverse('item_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name="dispatch")
class Item_Delete(DeleteView):
    model = Inventory
    template_name = 'item_delete.html'
    success_url = "/item/"


@method_decorator(login_required, name="dispatch")
def Item_Show(request, item_id):
    items = Item.objects.get(id=item_id)
    return render(request, 'item_show.html', {'items': items})