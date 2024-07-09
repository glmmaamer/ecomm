from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price: ':str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            cart_user = str(self.cart)
            cart_user = cart_user.replace("\'","\"")
            current_user.update(cart_old=str(cart_user))


    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price: ':str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            cart_user = str(self.cart)
            cart_user = cart_user.replace("\'","\"")
            current_user.update(cart_old=str(cart_user))

            
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
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        our_cart = self.cart
        #update quantity
        our_cart[product_id] = product_qty
        self.session.modified = True
        thing = self.cart
        return thing
    
 
    
    def delet(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            cart_user = str(self.cart)
            cart_user = cart_user.replace("\'","\"")
            current_user.update(cart_old=str(cart_user))

            
        
