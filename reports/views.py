from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime
from products.models import Product
from .models import ProductReport, InventoryReport

# Create your views here.

def reports(request):
    return render(request, 'reports/reports.html')

@login_required
def reports_dashboard(request):
    # Get recent reports
    recent_product_reports = ProductReport.objects.all()[:5]
    recent_inventory_reports = InventoryReport.objects.all()[:5]

    # Get quick stats
    low_stock_products = Product.objects.filter(stock_quantity__lt=10).count()
    out_of_stock_products = Product.objects.filter(stock_quantity=0).count()

    context = {
        'recent_product_reports': recent_product_reports,
        'recent_inventory_reports': recent_inventory_reports,
        'low_stock_products': low_stock_products,
        'out_of_stock_products': out_of_stock_products,
    }
    return render(request, 'reports/dashboard.html', context)

@login_required
def generate_product_report(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        try:
            product = Product.objects.get(pk=product_id)
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            
            report = ProductReport.objects.create(
                product=product,
                start_date=start_date,
                end_date=end_date,
                created_by=request.user
            )
            
            messages.success(request, 'Product report generated successfully!')
            return redirect('reports:product_report_detail', pk=report.pk)
            
        except Exception as e:
            messages.error(request, f'Error generating report: {str(e)}')
    
    products = Product.objects.all()
    return render(request, 'reports/generate_product_report.html', {'products': products})

@login_required
def generate_inventory_report(request):
    try:
        total_products = Product.objects.count()
        total_value = Product.objects.aggregate(
            total=Sum('price', field='price * stock_quantity')
        )['total'] or 0
        
        low_stock = Product.objects.filter(stock_quantity__lt=10).count()
        out_of_stock = Product.objects.filter(stock_quantity=0).count()
        
        report = InventoryReport.objects.create(
            date=timezone.now().date(),
            total_products=total_products,
            total_value=total_value,
            low_stock_items=low_stock,
            out_of_stock_items=out_of_stock,
            created_by=request.user
        )
        
        messages.success(request, 'Inventory report generated successfully!')
        return redirect('reports:inventory_report_detail', pk=report.pk)
        
    except Exception as e:
        messages.error(request, f'Error generating report: {str(e)}')
        return redirect('reports:dashboard')

@login_required
def product_report_detail(request, pk):
    report = ProductReport.objects.get(pk=pk)
    return render(request, 'reports/product_report_detail.html', {'report': report})

@login_required
def inventory_report_detail(request, pk):
    report = InventoryReport.objects.get(pk=pk)
    return render(request, 'reports/inventory_report_detail.html', {'report': report})
