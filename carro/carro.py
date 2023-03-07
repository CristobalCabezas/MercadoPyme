from decimal import Decimal
from django.conf import settings
from listelement.models import Producto

class Carro(object):

    def __init__(self, request):
    

        self.session = request.session  
        carro = self.session.get(settings.CART_SESSION_ID)

        if not carro:
            carro = self.session[settings.CART_SESSION_ID] = {}
        
        self.carro = carro


    def __iter__(self):

        element_ids = self.carro.keys()

        elements = Producto.objects.filter(id__in=element_ids)
        carro = self.carro.copy()

        for element in elements:
            carro[str(element.id)]['element'] = element
        
        for item in carro.values():
            item['precio_producto'] = int(item['precio_producto'])
            item['total_price'] = int(item['precio_producto'] * item['quantity'])
            yield item
    
    def __len__(self):

        return sum(item['quantity'] for item in self.carro.values())

    def get_total_price(self):

        return sum(int(item['precio_producto']) * item['quantity'] for item in self.carro.values())

    def add(self, element, quantity=1, overrride_quantity=False):

        element_id = str(element.id)
        
        if element_id not in self.carro:
            self.carro[element_id] = {'quantity':0, 'precio_producto':str(element.precio_producto)}

        if overrride_quantity:
            self.carro[element_id]['quantity'] = quantity
        else:
            self.carro[element_id]['quantity'] += quantity

        self.save()
    
    def save(self):
        self.session.modified = True


    
    def remove(self, element):

        element_id = str(element.id)

        if element_id in self.carro:
            del self.carro[element_id]
        
        self.save()

    def clear(self):
        del self.session.get[settings.CART_SESSION_ID]
        self.save()












    

