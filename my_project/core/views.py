from django.shortcuts import render, redirect
from .models import Cart, CartItem, Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    my_prod = Product.objects.all()
    return render(request, 'core/index.html', {
        'product': my_prod
    })


def add_to_cart(request, product_id): 
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(customer=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({
        'cart_count': cart.total_items(),
        'cart_total': float(cart.total_price())
    })


def login(request):
    if request.user.is_authenticated: 
        return redirect('index')

    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else: 
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def cart(request): 
    return render(request, 'core/cart.html')



def cart_detail(request):
    cart, created = Cart.objects.get_or_create(customer=request.user)
    items = cart.cartitem_set.select_related("product")
    return render(request, "core/cart_detail.html", {
        "cart": cart,
        "items": items,
    })
    
    
def password_reset(request): 
    return render(request, 'core/password_reset.html')