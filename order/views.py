from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
import datetime

# Create your views here.
from author.models import Author
from book.models import Book
from order.models import Order

from .forms import OrderUpdate

def addOrders(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
          
    if request.method == 'POST' and request.POST.get("form_type") == 'formConf':
        id = request.POST.get('id')
        current_order = Order.get_by_id(id)
        end_at = datetime.datetime.now()
        current_order.update(end_at=end_at)
        curent_book = Book.get_by_id(current_order.book_id)
        curent_book.count += 1
        curent_book.save()
        messages.success(request, 'The order has been confirmed')
        return redirect('addOrders')
    
    orders = Order.objects.order_by('-id')
    contex = {'title': 'Orders list', 'Orders': orders}
    return render(request, 'order/index.html', contex)
    
def editOrder(request, id):
     if request.method == 'POST':
        current_order = Order.get_by_id(id)
        orders = Order.objects.order_by('-id')
        edit = id
        form = OrderUpdate(request.POST)
        contex = {'title': 'Orders list', 'Order': current_order, 'form': form, 'Orders': orders, 'edit': edit}
        return render(request, 'order/index.html', contex)
    
def closeOrder(request, id):
     if request.method == 'POST':    
        current_order = Order.get_by_id(id)
        end_at = datetime.datetime.now()
        current_order.update(end_at=end_at)
        curent_book = Book.get_by_id(current_order.book_id)
        curent_book.count += 1
        curent_book.save()
        messages.success(request, 'The order has been confirmed')
        return redirect('addOrders')
    
def updateOrder(request, id):
     if request.method == 'POST':
        end_at = request.POST.get('end_at') 
        plated_end_at = request.POST.get('plated_end_at')
        order = Order.get_by_id(id)
        order.update(end_at, plated_end_at)
        messages.warning(request, 'The book has been change')
     else:
        messages.error(request, 'Something went wrong')

     return redirect('addBooks')        