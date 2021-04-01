from django.urls import path
from . import views

urlpatterns = [
    path('authors/',views.addAuthors, name = 'addAuthors'),
    path('books-list/',views.addBooks, name = 'addBooks'),
    path('delete/<int:id>/',views.delAuthors, name = 'delAuthors'),
    path('author-id-<int:id>/',views.editAuthors, name = 'editAuthors'),
    path('update-author-<int:id>/',views.updateAuthors, name = 'updateAuthors'),

]
