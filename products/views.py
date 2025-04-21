from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Product
from .forms import ProductForm

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
