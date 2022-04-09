from django.urls import path
from book.views import *


app_name = 'book'

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('seller-dashboard/', SellerDashboardView.as_view(), name='seller-dashboard'),
    path('user-dashboard/', UserDashboardView.as_view(), name='user-dashboard'),

    path('my-orders/', MyOrdersView.as_view(), name='my-orders'),
    path('user-order/<str:book_id>', UserOrderView.as_view(), name='user-order'),
    
    

    
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('update-book/<str:book_id>', UpdateBookView.as_view(), name='update-book'),
    path('delete-book/<str:book_id>', DeleteBookView.as_view(), name='delete-book'),

]
