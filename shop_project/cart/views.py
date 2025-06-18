from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CartAddProductForm, OrderForm
from shop.models import Product
from .cart import Cart

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
            messages.success(request, 'Заказ успешно создан!')
            return redirect('cart:cart_detail')
    else:
        order_form = OrderForm()
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'order_form': order_form})

@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product_id=product.id, quantity=cd['quantity'], reload=cd['reload'])
            messages.success(request, 'Товар добавлен в корзину!')
            return redirect('cart:cart_detail')
    else:
        form = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})

def remove_from_cart(request, product_id): 
    cart = Cart(request)
    try:
        cart.remove(product_id)
        messages.success(request, 'Товар удален из корзины!')
    except:
        messages.error(request, 'Ошибка при удалении товара.')
    return redirect('cart:cart_detail')