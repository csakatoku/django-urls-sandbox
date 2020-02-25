from django.http import HttpResponse


def top(request):
    return HttpResponse('sandbox.app_b.subapp_b')
