from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AddAuthorInfo
from .models import Author
from book.models import Book

def addAuthors(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    
    form = AddAuthorInfo(request.POST or None)
    if request.method == 'POST' and request.POST.get("form_type") == 'formAdd':
        form = AddAuthorInfo(request.POST)
    
        name = request.POST.get('name') 
        surname = request.POST.get('surname')        
        patronymic = request.POST.get('patronymic')        
        
        if name != "" and surname != "" and patronymic != "":
            Author.create(name, surname, patronymic)
            messages.success(request, 'The author has been added')
            return redirect('addAuthors')
        else:
            messages.error(request, 'An error occurred while adding. Please try again')
    
    if request.method == 'POST' and request.POST.get("form_type") == 'formDel':
        id = request.POST.get('id')
        Author.delete_by_id(id)
        messages.error(request, 'The author has been removed')
        return redirect('addAuthors')
        
    authors = Author.objects.order_by('-id')
    contex = {'title': 'Authors', 'Authors': authors, 'form': form}
    return render(request, 'book/authors.html', contex)

def delAuthors(request, id):
     if request.method == 'POST':
        author = Author.get_by_id(id)
        author.delete_by_id(id)
        messages.error(request, 'The author has been removed')
        return redirect('addAuthors')

def editAuthors(request, id):
     if request.method == 'POST':
        author = Author.get_by_id(id)
        authors = Author.objects.order_by('-id')
        form = AddAuthorInfo()
        edit = id
        contex = {'title': 'Authors', 'Authors': authors, 'author':author, 'form': form, 'edit': edit}
        return render(request, 'book/authors.html', contex)

def updateAuthors(request, id):
     if request.method == 'POST':
        name = request.POST.get('name') 
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic') 
        author = Author.get_by_id(id)
        author.update(name, surname, patronymic)
        messages.success(request, 'The author has been change')
     else:
        messages.error(request, f'Something went wrong {name} {surname} {patronymic}')

     return redirect('addAuthors')
    

def addBooks(request):    
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST' and request.POST.get("form_type") == 'formAdd':
        form = AddAuthorInfo(request.POST)
    
        name = request.POST.get('name') 
        description = request.POST.get('description')        
        count = request.POST.get('count')        
        authors = []  
        for el in request.POST:
            if 'author' in el:
                authors.append(request.POST.get(el))
        if name != "" and description != "":
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
    contex = {'title': 'Books', 'Authors': authors, 'Book': books}
    return render(request, 'book/books.html', contex)
    