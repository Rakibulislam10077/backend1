from rest_framework import serializers
from . models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'roll', 'address', 'phone', 'email', 'image']

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     roll = serializers.IntegerField()
#     address = serializers.CharField(max_length=200)
#     phone = serializers.CharField(max_length=11)
#     email = serializers.CharField(max_length=100)
#     image = serializers.ImageField()
    
    
#     def create(self, validated_data):
#         return Students.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
        
#         instance.save()
#         return instance