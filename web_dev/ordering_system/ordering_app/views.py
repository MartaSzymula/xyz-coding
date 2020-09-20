from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Order, Product, OderLine

class IndexView(View):
    def get(self, request):
        orders = Order.objects.all()

        context = {
            'orders': orders
        }

        return render(request, 'index.html', context)


class ProductView(View):
    def post(self,request):

        Product.objects.create(
        name = request.POST.get('name'),
        description = request.POST.get('description'),
        quantity = request.POST.get('quantity'),
        )

        return redirect('/')

class OrderView(View):
    def post(self,request):

        Order.objects.create(
        order_number = request.POST.get('order_number'),
        is_fulfilled = False,
        is_shipped = False
        )

        return redirect('/')


class OrderDetailView(View):

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        all_products = Product.objects.all()
        #Get all order line items for orders
        items = OderLine.objects.filter(order=order).select_related('product')

        context = {
        'order': order,
        'all_products': all_products,
        'items': items,
        }

        return render(request, 'order.html', context)


    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        product = Product.objects.get(id=request.POST.get('product'))
        quantity = request.POST.get('quantity')

        OderLine.objects.create(
        order=order,
        product=product,
        quantity=quantity
        )

        return redirect(f'/orders/{order_id}/')
