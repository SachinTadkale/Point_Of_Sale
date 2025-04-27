from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.decorators import login_required, user_passes_test # type: ignore
from django.contrib import messages # type: ignore
from django.core.exceptions import PermissionDenied # type: ignore
from .models import Product, Order
from .forms import ProductForm
from django.core.mail import send_mail # type: ignore
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone

# Create your views here.

def products(request):
  return render(request,'products/products.html')

def is_admin(user):
    return user.role == 'admin'

def our_products(request):
    products = Product.objects.all()
    return render(request, 'products/our_products.html', {'products': products})

@login_required
@user_passes_test(is_admin, login_url='/auth/login/')
def inventory(request):
    if not request.user.role == 'admin':
        messages.error(request, 'You do not have permission to access the inventory.')
        return redirect('products:our_products')
    products = Product.objects.all()
    return render(request, 'products/inventory.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
@user_passes_test(is_admin, login_url='/auth/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('products:inventory')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Add Product'})

@login_required
@user_passes_test(is_admin, login_url='/auth/login/')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('products:inventory')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Update Product'})

@login_required
@user_passes_test(is_admin, login_url='/auth/login/')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('products:inventory')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

@login_required
def buy_now(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.stock_quantity <= 0:
        messages.error(request, 'Sorry, this product is out of stock.')
        return redirect('products:product_detail', pk=pk)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            product=product,
            amount=product.price,
            status='pending'
        )
        subject = f'Purchase Confirmation for {product.name}'
        html_message = render_to_string('products/email_purchase_confirmation.html', {
            'user': request.user,
            'product': product,
            'order': order,
        })
        plain_message = strip_tags(html_message)
        from_email = None  # Uses DEFAULT_FROM_EMAIL
        to = [request.user.email]
        send_mail(
            subject,
            plain_message,
            from_email,
            to,
            html_message=html_message,
            fail_silently=False,
        )
        return redirect('products:purchase_success', pk=product.pk)

    return render(request, 'products/dummy_payment.html', {'product': product})

@login_required
def purchase_success(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/purchase_success.html', {'product': product})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'products/my_orders.html', {'orders': orders})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.role == 'admin')
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'products/all_orders.html', {'orders': orders})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.role == 'admin')
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            # Only reduce stock and send email if changing from not delivered to delivered
            if new_status == 'delivered' and order.status != 'delivered':
                if order.product.stock_quantity > 0:
                    order.product.stock_quantity -= 1
                    order.product.save()
                subject = f'Your product "{order.product.name}" has been delivered!'
                html_message = render_to_string('products/email_product_delivered.html', {
                    'order': order,
                    'now': timezone.now(),
                })
                plain_message = strip_tags(html_message)
                from_email = None  # Uses DEFAULT_FROM_EMAIL
                to = [order.user.email]
                send_mail(
                    subject,
                    plain_message,
                    from_email,
                    to,
                    html_message=html_message,
                    fail_silently=False,
                )
            order.status = new_status
            order.save()
            messages.success(request, 'Order status updated.')
    return redirect('products:all_orders')

@login_required
@user_passes_test(lambda u: u.is_superuser or u.role == 'admin')
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully.')
    return redirect('products:all_orders')
