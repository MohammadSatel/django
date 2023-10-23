from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def index(req):
    return JsonResponse('home', safe=False)


def about(req):
    return JsonResponse('about page', safe=False)


def books(req):
    return JsonResponse('books page', safe=False)


def customers(req):
    return JsonResponse('customers page', safe=False)


def loans(req):
    return JsonResponse('loans page', safe=False)
