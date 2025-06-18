from decimal import Decimal
from django.conf import settings
from shop.models import Product
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CartAddProductForm, OrderForm
from shop.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = {
            str(k): {'quantity': str(v.get('quantity', '0')), 'price': str(v.get('price', '0.00'))}
            for k, v in cart.items()
        }

    def add(self, product_id, quantity=1, reload=False):
        product_id = str(product_id)
        try:
            product = Product.objects.get(id=product_id)
            if not product.is_available:
                raise ValueError("Товар недоступен")
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity': '0', 'price': str(product.price)}
            current_quantity = int(self.cart[product_id]['quantity'])
            new_quantity = quantity if reload else max(0, current_quantity + int(quantity)) 
            self.cart[product_id]['quantity'] = str(new_quantity)
            self.save()
        except Product.DoesNotExist:
            raise ValueError("Товар не найден")
        except ValueError as e:
            raise e

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])  
            item['quantity'] = int(item['quantity'])  
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * int(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def save(self):
        cart_data = {
            str(k): {'quantity': str(v['quantity']), 'price': str(v['price'])}
            for k, v in self.cart.items()
        }
        self.session['cart'] = cart_data
        self.session.modified = True


@login_required
def cart_detail(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            from shop.models import Order, OrderItem
            order = Order.objects.create(
                user=request.user,
                total_price=cart.get_total_price(),
                pickup_method=order_form.cleaned_data['pickup_method']
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            subject = 'Ваш заказ успешно оформлен'
            message = f'Уважаемый {request.user.username},\n\nВаш заказ #{order.id} успешно оформлен.\nОбщая сумма: {order.total_price} руб.\nСпособ получения: {order.get_pickup_method_display()}\n\nСпасибо за покупку!'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = request.user.email
            send_mail(subject, message, from_email, [to_email], fail_silently=True)
            return redirect('cart:cart_detail')
    else:
        order_form = OrderForm()
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'order_form': order_form})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            try:
                cart.add(product_id=product.id, quantity=quantity)
                return redirect('cart:cart_detail')
            except ValueError:
                pass  
        else:
            pass 
    else:
        form = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form, 'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)
    try:
        cart.remove(product_id)
    except:
        pass  
    return redirect('cart:cart_detail')