from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!12345')


def second_page(request):
    return HttpResponse('А это вторая страница!')
