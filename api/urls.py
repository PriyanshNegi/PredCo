from django.urls import include, path
from django import urls
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # path('timer-update/<int:pk>', lesson_timer_update, name='lesson-timer-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)