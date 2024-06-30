from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price: ':str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        
    
    def cart_total(self):
        product_ids = self.cart.keys()
        productes = Product.objects.filter(id__in=product_ids)
        quantites = self.cart    
        total = 0
        for key, value in quantites.items():
            key = int(key)
            for product in productes:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
            
    def get_quantites(self):
        quantites = self.cart
        return quantites
    
 
    
    def delet(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        now_cart = self.cart
        #update quantity
        now_cart[product_id] = product_qty
        self.session.modified = True
        update_quantity = self.cart
        return update_quantity

            
    
