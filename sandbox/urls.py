from django.urls import path, include

urlpatterns = [
    path('a/', include('sandbox.app_a.urls')),
    path('b/', include('sandbox.app_b.urls')),
]
