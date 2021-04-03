from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from django.contrib.auth import authenticate, login, logout

from order.models import Order
from author.models import Author
from book.models import Book
from authentication.models import CustomUser


from .forms import AddBookInfo
from authentication.forms import CreateUserForm

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
    
def addBooks(request):    
     user = request.user
     if not user.is_authenticated:
         return redirect('home')
    
     form = AddBookInfo(request.POST or None)
     if request.method == 'POST' and request.POST.get("form_type") == 'formAdd':
    
         name = request.POST.get('name') 
         description = request.POST.get('description')        
         count = request.POST.get('count')        
         authors = []  
         for el in request.POST:
             if 'author' in el:
                 authors.append(request.POST.get(el))
         if form.is_valid():
             if len(authors) >= 1 and authors[0] != 'None':
                 Book.create(name, description, count, authors)
             else:
                 Book.create(name, description, count)
             messages.success(request, f'The Book has been added')
             return redirect('addBooks')
         else:
             messages.error(request, 'An error occurred while adding. Please try again')
    
     if request.method == 'POST' and request.POST.get("form_type") == 'formDel':
         id = request.POST.get('id')
         Book.delete_by_id(id)
         messages.error(request, 'Book has been removed')
         return redirect('addBooks')
    
     authors = Author.objects.order_by('-id')
     books = Book.objects.order_by('-id')
     contex = {'title': 'Books', 'Authors': authors, 'form':form, 'Book': books}
     return render(request, 'book/books.html', contex)

def delBook(request, id):
     if request.method == 'POST':
        book = Book.get_by_id(id)
        book.delete_by_id(id)
        messages.error(request, 'The book has been removed')
        return redirect('addBooks')

def moreInfoBook(request, id):
     if request.method == 'POST':
        book = Book.get_by_id(id)
        name = book.name
        authors = Author.objects.order_by('-id')
        order = Order.objects.filter(book_id=id).order_by('-id')
        contex = {'title': f'Book: "{book.name}"', 'Orders': order, 'Authors':authors,  'Book': book}
        return render(request, 'book/info.html', contex)
    
def editBooks(request, id):
     if request.method == 'POST':
        book = Book.get_by_id(id)
        authors = Author.objects.order_by('-id')
        books = Book.objects.order_by('-id')
        user_authors = []  
        for author in book.authors.all():
                user_authors.append(author)
        contex = {'title': 'Books', 'Authors': authors, 'Book': books, 'Edit': book, 'UserAuthor': user_authors}
        return render(request, 'book/books.html', contex)    
    
def updateBook(request, id):
     if request.method == 'POST':
        name = request.POST.get('name') 
        description = request.POST.get('description')
        count = request.POST.get('count') 
        book = Book.get_by_id(id)
        book.update(name, description, count)

        messages.warning(request, 'The book has been change')
     else:
        messages.error(request, 'Something went wrong')

     return redirect('addBooks')    
    
def userinfo(request):   
     user = request.user
    
     if not user.is_authenticated:
         return redirect('home')
    
     id = user.id
     books = Book.objects.order_by('-id') 
     authors = Author.objects.order_by('-id')
     order = Order.objects.filter(user_id=id).order_by('-end_at')
     contex = {'title': 'Profile', 'Orders': order, 'Authors':authors,  'Book': books, 'User': user}
     return render(request, 'book/profile.html', contex)    

def closeUserOrder(request, id):
     if request.method == 'POST':    
        current_order = Order.get_by_id(id)
        end_at = datetime.datetime.now()
        current_order.update(end_at=end_at)
        curent_book = Book.get_by_id(current_order.book_id)
        curent_book.count += 1
        curent_book.save()
        messages.success(request, 'The order has been confirmed')
        return redirect('userinfo')
    
def editUser(request, id):
    user = request.user
    edit = id
    form = CreateUserForm(request.POST)
    contex = {'title': 'Edit user', 'User': user, 'Edit': edit, 'form':form}
    return render(request, 'book/profile.html', contex)

def updateUser(request):
     if request.method == 'POST':
         id = request.user.id
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         middle_name = request.POST.get('middle_name')
         password = request.POST.get('password1')
         password_confirm = request.POST.get('password2')

         user = CustomUser.get_by_id(id)
         if password != password_confirm:
            messages.error(request, 'Confirming password does not match')
            return redirect('editUser', id)
         if password:
            user.update(first_name=first_name, last_name=last_name, middle_name=middle_name, password=password )
         else:
            user.update(first_name=first_name, last_name=last_name, middle_name=middle_name )

         messages.warning(request, f"User {user.email} has been changed")
     else:
        messages.error(request, 'Something went wrong')

     return redirect('userinfo')