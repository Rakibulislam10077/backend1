from rest_framework import serializers
from .models import Teachers

class TeacherSerializers(serializers.Serializer):
    class Meta:
        model = Teachers
        fields = ['name', 'subject', 'gender']