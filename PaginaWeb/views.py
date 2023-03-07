from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from carro.carro import Carro
from django.http import HttpResponseNotFound, JsonResponse
from listelement.models import Producto, Categoria
from decimal import Decimal


# Create your views here.
def index(request):

   search = request.GET.get('search')
   category_id = request.GET.get('id')

   

   if search:  
      elements = Producto.objects.filter(nombre_producto__icontains=search)
   else:
      elements = Producto.objects

   


   elements = elements.all()
   paginator = Paginator(elements, 5)
   categories = Categoria.objects.all()



   page_number = request.GET.get('page')
   elements_page = paginator.get_page(page_number)

   return render(request, 'index.html', {'elements' : elements_page})


def detail(request, url_clean):
   element = get_object_or_404(Producto, url_clean=url_clean)
  
   if request.method == 'GET' and request.GET.get('quantity'): 
      carro = Carro(request)
      carro.add(element, int(request.GET.get('quantity')))
      
      return redirect ('PaginaWeb:detail', url_clean)
   return render(request,'detail.html', {'producto':element})


#carro

def carro_detail(request):
   return render(request, 'carro/detail.html',{'carro' : Carro(request) })

def carro_remove(request, pk):
   carro = Carro(request)
   element = get_object_or_404(Producto, pk=pk)

   carro.remove(element)
   return redirect('PaginaWeb:cart_detail')

def carro_size(request):
   cart = Carro(request)
   return JsonResponse({'size' : len(cart)}) 

   


