from django.urls import path

from ..views import a_views as views


app_name = 'subapp_a'

urlpatterns = [
    path('', views.top, name='top'),
]
