from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('books/<int:id>', views.view_book),
    path('add-book', views.add_book),
    path('add-book-to-author',views.add_book_to_author),
    path('authors', views.authors),
    path('authors/<int:id>', views.view_author),  
    path('add-author', views.add_author),
    path('add-author-to-book',views.add_author_to_book)
]
         