from django.http import HttpResponse


def top(request):
    return HttpResponse('sandbox.app_c.views.a_views')
