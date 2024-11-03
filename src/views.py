from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



def login_view(request):
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'main.html', {})


def find_user_view(request):
    return JsonResponse({'success': True})