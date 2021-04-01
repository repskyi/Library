from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from django.contrib.auth import authenticate, login, logout

from .models import Author, Book
from order.models import Order

# Create your views here.
def index(request):
    user = request.user
    avaliable_order = Order.get_all()
    
    if request.method == 'POST':
        book_id = request.POST.get('id') 
        order_book = Book.get_by_id(book_id)
        created = datetime.datetime.now()
        plated_end_at = created + datetime.timedelta(days=19)
        Order.create(user, order_book, str(plated_end_at))
        messages.success(request, 'The book is added to the orders')
        order_book.count -= 1
        order_book.save()
        return redirect('home')
    
    authors = Author.objects.order_by('-id')
    books = Book.objects.order_by('-id')
    contex = {'title': 'Books list', 'Authors': authors, 'Book': books, 'User': user, 'Ordered': avaliable_order}
    return render(request, 'book/index.html', contex)
    

    
    
    
    
    
    
    
