from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def index(req):
    return Response("home")


@api_view(['GET','POST'])
def about(req):
    return Response('about page')


@api_view(['GET','POST'])
def books(req):
    return Response('books page')


@api_view(['GET','POST'])
def customers(req):
    return Response('customers page')


@api_view(['GET','POST'])
def loans(req):
    return Response('loans page')
