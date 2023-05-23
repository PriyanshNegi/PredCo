from django.urls import include, path
from django import urls
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('client-admin/', ClientAdminView.as_view(), name='client-admin'),
    path('add-client/', AddOrgView.as_view(), name='add-client'),
    path('delete-client/<str:pk>', RemoveClient.as_view(), name='delete-client'),

    path('dashboard/<str:slug>', DashboardView.as_view(), name='dashboard'),
    path('add-usecase/<str:slug>', AddUseCaseView.as_view(), name='add-usecase'),
    path('delete-usecase/<str:pk>/<str:org_slug>', RemoveUseCase.as_view(), name='delete-usecase'),

    path('usecase/<str:slug>', UseCaseView.as_view(), name='usecase'),
    path('add-sensor/<str:slug>', AddSensorView.as_view(), name='add-sensor'),
    path('delete-sensor/<str:pk>/<str:usecase_slug>', RemoveSensor.as_view(), name='delete-sensor'),
    path('update-sensor/<str:pk>/<str:usecase_slug>/<str:status>', UpdateSensorStatus.as_view(), name='update-sensor'),

    path('embed-dashboard/<str:slug>', EmbedDashboardView.as_view(), name='embed-dashboard'),
    # path('refresh-alerts', EmbedDashboardView.as_view(), name='embed-dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)