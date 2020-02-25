from django.http import HttpResponse


def top(request):
    return HttpResponse('sandbox.app_a.subapp_c')
