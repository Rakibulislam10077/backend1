from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teachers
from . serializers import TeacherSerializers


# Create your views here.
@api_view(
    ['GET']
)
def teacher_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            tc = Teachers.objects.get(id=id)
            serializer = TeacherSerializers(tc)
            return Response(serializer.data)
        tc = Teachers.objects.all()
        serializer = TeacherSerializers(tc, many=True)
        return Response(serializer.data)