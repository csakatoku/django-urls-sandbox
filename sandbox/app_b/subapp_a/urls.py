from django.urls import path

from . import views


app_name = 'subapp_a'

urlpatterns = [
    path('', views.top, name='top'),
]
