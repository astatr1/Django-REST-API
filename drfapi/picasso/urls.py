from django.urls import path

from . import views
app_name = 'api'

urlpatterns = [
    path('files/', views.FileAPIView.as_view(), name='files_list'),
]