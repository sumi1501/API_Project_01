from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

def Schooljson(request):
    SOD=School.objects.all()
    JOD=Schoolmodel(SOD,many=True)
    jsondata=JOD.data

    return Response(jsondata)