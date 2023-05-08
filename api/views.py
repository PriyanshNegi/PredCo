from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import *
from .forms import *

class DashboardView(View):
    def get(self, request, format=None):
        return render(request, 'dashboard/home.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        if 'login_page' in request.POST:
            next = request.POST.get('next')
            username = request.POST['username']
            password = request.POST['password']
            context = {
                'user_found': True,
                'user_name': username
            }
            if username and password:
                if User.objects.filter(username=username).exists():
                    user = auth.authenticate(
                        username=username, password=password)
                    if user:
                        if user.is_active:
                            auth.login(request, user)
                            
                            if next:
                                return redirect(next)
                            return redirect("dashboard")

                        messages.error(
                            request, "Account is not active,please check your email"
                        )

                elif User.objects.filter(email=username).exists():
                    user = User.objects.get(email=username)
                    user = auth.authenticate(
                        username=user.username, password=password)
                    if user:
                        if user.is_active:
                            auth.login(request, user)
                            
                            if next:
                                return redirect(next)
                            return redirect("dashboard")

                        messages.error(
                            request, "Account is not active,please check your email"
                        )
                elif (User.objects.filter(email=username).exists() or User.objects.filter(username=username).exists() == False):
                    messages.error(
                        request, "The username or Email you have entered does not exist.")
                    return render(request, 'login.html', context)

            context = {
                'user_found': True,
                'user_name': username
            }
            messages.error(request, 'Invalid credentials, try again')
            return render(request, 'login.html', context)

        return render(request, "login.html")


def logout(request):
    LoginHistory.objects.create(user=request.user, logged_in=False)
    auth.logout(request)
    return redirect('dashboard')
