from django.urls import include, path


app_name = 'app_a'

urlpatterns = [
    path('a/', include('sandbox.app_a.subapp_a.urls')),
    path('b/', include('sandbox.app_a.subapp_b.urls')),
]
