from django.urls import include, path


urlpatterns = [
    path('a/', include('sandbox.app_b.subapp_a.urls')),
    path('b/', include('sandbox.app_b.subapp_b.urls')),
]
