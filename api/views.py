from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import *
from .forms import *


"""
    AUTHENTICATION VIEWS
"""


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

                            return redirect("client-admin")

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

                            return redirect("client-admin")

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

    return redirect('login')


"""
    ADMIN OPERATION VIEWS
"""


class ClientAdminView(View):
    def get(self, request, format=None):
        orgs = Org.objects.filter(our_admin=request.user)
        form = OrgForm()

        return render(request, 'dashboard/home.html', 
            {
                'orgs': orgs, 
                'form': form
            }
        )

class AddOrgView(View):
    def post(self, request, format=None):
        admin = request.user
        form = OrgForm(request.POST, request.FILES)
        if form.is_valid():
            org = form.save(commit=False)
            org.our_admin = admin
            org.save()

            return redirect('client-admin')

        return redirect('client-admin')

class RemoveClient(View):
    def get(self, request, pk):
        Org.objects.filter(key=pk).first().delete()

        return redirect('client-admin')


"""
    CLIENT OPERATION VIEWS
"""


class DashboardView(View):
    def get(self, request, slug):
        org = Org.objects.filter(key=slug).first()
        uses = UseCase.objects.filter(org=org)
        usecases = [{'usecase': use, 'sensors': len(Sensor.objects.filter(usecase=use))} for use in uses]
    
        form = UseCaseForm()

        return render(request, 'dashboard/dashboard.html', 
            {
                'org': org, 
                'form': form, 
                'uses': usecases
            }
        )

class UseCaseView(View):
    def get(self, request, slug):
        usecase = UseCase.objects.filter(key=slug).first()
        sensors = Sensor.objects.filter(usecase=usecase)
        
        form = SensorForm()

        return render(request, 'dashboard/usecase.html', 
            {
                'usecase': usecase, 
                'form': form, 
                'sensors': sensors,
                'active': len(sensors.filter(active=True))        
            }
        )


class AddSensorView(View):
    def post(self, request, slug):
        usecase = UseCase.objects.filter(key=slug).first()
        form = SensorForm(request.POST, request.FILES)
        if form.is_valid():
            Sensor = form.save(commit=False)
            Sensor.usecase = usecase
            Sensor.save()

            return redirect('usecase', slug=slug)

        return redirect('usecase', slug=slug)
        
class RemoveSensor(View):
    def get(self, request, pk, usecase_slug):
        Sensor.objects.filter(key=pk).first().delete()

        return redirect('usecase', slug=usecase_slug)

class UpdateSensorStatus(View):
    def get(self, request, pk, usecase_slug, status):
        sensor = Sensor.objects.filter(key=pk).first()
        sensor.active = True if status=="True" else False
        sensor.save(update_fields=['active'])

        return redirect('usecase', slug=usecase_slug)

class AddUseCaseView(View):
    def post(self, request, slug):
        org = Org.objects.filter(key=slug).first()
        form = UseCaseForm(request.POST, request.FILES)
        if form.is_valid():
            UseCase = form.save(commit=False)
            UseCase.org = org
            UseCase.save()

            return redirect('dashboard', slug=slug)

        return redirect('dashboard', slug=slug)

class RemoveUseCase(View):
    def get(self, request, pk, org_slug):
        UseCase.objects.filter(key=pk).first().delete()

        return redirect('dashboard', slug=org_slug)


class EmbedDashboardView(View):
    def post(self, request, slug):
        usecase = UseCase.objects.filter(key=slug).first()
        usecase.iframe_link = request.POST.get('dashboard_link')
        usecase.save(update_fields=['iframe_link'])

        return redirect('usecase', slug=slug)

# base_url = "https://<your-cloud-id>.cloud.elastic.co"
# username = "<your-username>"
# password = "<your-password>"

# class RefreshAlertView(View):
#     def post(self, request, format=None):
#         url = f"{base_url}/.alerts-*/_search"
#         headers = {
#             "Content-Type": "application/json"
#         }
#         auth = (username, password)
#         query = {
#             "query": {
#                 "match_all": {}
#             }
#         }
#         response = requests.get(url, json=query, headers=headers, auth=auth)
#         if response.status_code == 200:
#             alerts = response.json()['hits']['hits']
#             print(alerts)
#             return redirect('dashboard')
#         else:
#             print(f"Error: {response.text}")
#             return redirect('dashboard')