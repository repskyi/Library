from django.shortcuts import render, redirect
from django.contrib import messages
import datetime

# Create your views here.
from .models import Author, Book
from order.models import Order

def addOrders(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
          
    if request.method == 'POST' and request.POST.get("form_type") == 'formConf':
        id = request.POST.get('id')
        current_order = Order.get_by_id(id)
        end_at = datetime.datetime.now()
        current_order.update(end_at=end_at)
        messages.error(request, 'The order has been confirmed')
        return redirect('addOrders')
    
    orders = Order.objects.order_by('-id')
    contex = {'title': 'Orders list', 'Order': orders}
    return render(request, 'order/index.html', contex)