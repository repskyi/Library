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
    
        name = request.POST.get('name') 
        surname = request.POST.get('surname')        
        patronymic = request.POST.get('patronymic')        
        
        if name != "" and surname != "" and patronymic != "":
            Author.create(name, surname, patronymic)
            messages.info(request, 'The author has been added')
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
        form = AddAuthorInfo(request.POST)
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
        messages.warning(request, 'The author has been change')
     else:
        messages.error(request, 'Something went wrong')

     return redirect('addAuthors')
    
