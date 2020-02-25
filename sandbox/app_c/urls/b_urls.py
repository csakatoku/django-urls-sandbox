from django.urls import path

from ..views import b_views as views


app_name = 'subapp_b'

urlpatterns = [
    path('', views.top, name='top'),
]
