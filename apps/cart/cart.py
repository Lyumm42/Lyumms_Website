from decimal import Decimal
from apps.products.models import Product
from django.conf import settings


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            print("DELETED")
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for p in products:
            cart[str(p.id)]["product"] = p

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["quantity"] * item["price"]
            yield item


    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
        total_count
        for item in self.cart_values():
            total_count += item["quantity"]
        return total_count


    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())
        total_sum =0
        for item in self.cart.values():
            total_sum += Decimal(item["price"]) * item["quantity"]
        return total_sum


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def save(self):
        self.session.modified = True
