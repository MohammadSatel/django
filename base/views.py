from django.http import JsonResponse

# Create your views here.
def index(req):
    return JsonResponse('hello home', safe=False)

def about(req):
    return JsonResponse('about page', safe=False)

def books(req):
    return JsonResponse('books page', safe=False)

def customers(req):
    return JsonResponse('customers page', safe=False)

def loans(req):
    return JsonResponse('loans page', safe=False)
