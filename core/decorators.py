from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_seller:
                return redirect('book:seller-dashboard')
            elif request.user.is_customer:
                return redirect('book:user-dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

