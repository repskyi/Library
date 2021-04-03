from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('profile/',views.userinfo, name = 'userinfo'),
    path('books-list/',views.addBooks, name = 'addBooks'),
    path('book-delete/<int:id>/',views.delBook, name = 'delBook'),
    path('book-id-<int:id>/',views.editBooks, name = 'editBooks'),
    path('info-book-id-<int:id>/',views.moreInfoBook, name = 'moreInfoBook'),
    path('update-book-<int:id>/',views.updateBook, name = 'updateBook'),
    path('close-user-order-<int:id>/',views.closeUserOrder, name = 'closeOrderUser'),
    path('edit-user-<int:id>/',views.editUser, name = 'editUser'),
    path('update-user/',views.updateUser, name = 'updateUser'),

    

]
