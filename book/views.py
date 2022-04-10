from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *



# Create your views here.


class SellerDashboardView(TemplateView, LoginRequiredMixin):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'book/dashboard.html'

    def get_context_data(self, **kwargs):
        my_book = Book.objects.filter(user=self.request.user)
        orders = Order.objects.filter(book_user=self.request.user.id)

        books = Book.objects.filter(user=self.request.user).order_by('date')[0:10]
        context = {'books': books, 'orders': orders }
        return context



class UserDashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'book/user_dashboard.html'
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'

    def get_context_data(self, **kwargs):
        books = Book.objects.all().order_by('date')[0:10]
        orders = Order.objects.filter(user=self.request.user).order_by('order_date')[0:5]
        context = {'books': books, 'orders':orders }
        return context

        

class AddBookView(TemplateView, LoginRequiredMixin):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    form_class = AddBookForm
    initial = {'key': 'value'}
    template_name = 'book/add_book.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            print(obj)
            obj.save()
            messages.success(request, 'Add Book Success ')
            return redirect('book:add-book')
        return render(request, self.template_name, {'form': form})


class UpdateBookView(TemplateView, LoginRequiredMixin):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    #form_class = AddBookForm
    #initial = {'key': 'value'}
    template_name = 'book/update_book.html'

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        form = AddBookForm(instance=book)
        context = {'form': form, 'book':book}
        return render(request, 'book/update_book.html', context)

    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        name = request.POST["name"]
        author = request.POST["author"]
        price = request.POST["price"]
        category = request.POST["category"]
        is_available = request.POST["is_available"]
        if is_available == 'on':
            is_available = True
        else:
            is_available= False

        form = AddBookForm(request.POST, instance=book)
        book = Book.objects.filter(pk=book_id).update(
            name=name, author=author, category=category, price=price, is_available=is_available
        )
        
        messages.success(request, 'Update Book Success ')
        return redirect('book:seller-dashboard')


class DeleteBookView(TemplateView, LoginRequiredMixin):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'book/seller-dashboard.html'

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return redirect('book:seller-dashboard')


class UserOrderView(TemplateView, LoginRequiredMixin):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'book/order.html'

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        context = {'book': book }
        return render(request, 'book/order.html', context)        

    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        order = Order.objects.create(book=book, user=request.user, book_user=book.user.id)
        return redirect('book:user-dashboard')


class MyOrdersView(TemplateView, LoginRequiredMixin):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'book/myorders.html'

    def get_context_data(self, **kwargs):
        orders = Order.objects.filter(user=self.request.user).order_by('order_date')
        context = {'orders': orders }
        return context

