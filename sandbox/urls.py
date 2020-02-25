from django.urls import path, include

urlpatterns = [
    path('a/', include('sandbox.app_a.urls')),
    path('b/', include('sandbox.app_b.urls')),
    path('c/a/', include('sandbox.app_c.urls.a_urls', namespace='subapp_c_a')),
    path('c/b/', include('sandbox.app_c.urls.b_urls', namespace='subapp_c_b')),
]
