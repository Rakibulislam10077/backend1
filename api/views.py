# from django.shortcuts import render
from . models import Students 
from .serializers import StudentSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
class students(GenericAPIView, ListModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class studentsCreate(GenericAPIView, CreateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class studentGetById(GenericAPIView, RetrieveModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    
    
class studentGetById(GenericAPIView, UpdateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class studentGetById(GenericAPIView, DestroyModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
# class student_create(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             st = Students.objects.get(id=id)
#             serializer = StudentSerializer(st)
#             return Response(serializer.data)
#         st = Students.objects.all()
#         serializer = StudentSerializer(st, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {'message': 'student created successfully'}
#             return Response(response)
#         return Response(serializer.errors)


#     def put(self, request, pk, format=None):
#         id = pk
#         st = Students.objects.get(id=id)
#         serializer = StudentSerializer(st, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return(Response({'message':'student updated successfully'}))
#         return(Response(serializer.errors))
        
#     def patch(self, request, pk, format=None):
#         id = pk
#         st = Students.objects.get(id=id)
#         serializer = StudentSerializer(st, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return(Response({'message':'partial student updated successfully'}))
#         return(Response(serializer.errors))
    
    
#     def delete(self,request, pk=None,format=None):
#         id = pk
#         st = Students.objects.get(id=id)
#         st.delete()
#         return Response({'message': 'Student delete successfully'})
        

# def students(request):
#     studentComplexData = Students.objects.all()
#     serialization = StudentSerializer(studentComplexData, many=True)
#     convert_serialization_to_json = JSONRenderer().render(serialization.data)
#     return HttpResponse(convert_serialization_to_json, content_type='application/json')
# def getStudentBy(request, pk):
#     studentComplexData = Students.objects.get(id=pk)
#     serialization = StudentSerializer(studentComplexData,)
#     convert_serialization_to_json = JSONRenderer().render(serialization.data)
#     return HttpResponse(convert_serialization_to_json, content_type='application/json')

# @csrf_exempt
# def create_student(request):
    # if request.method == 'POST':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     serializer = StudentSerializer(data=python_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'message': 'Successfully inserted data'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')
    
    # if request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id')
    #     st=Students.objects.get(id=id)
    #     serializer = StudentSerializer(st, data=python_data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'message': 'Successfully update data'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')
    
    # if request.method == 'DELETE':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id')
    #     st=Students.objects.get(id=id)
    #     st.delete()
    #     res = {'message': 'Successfully delete data'}
    #     json_data = JSONRenderer().render(res)
    #     return HttpResponse(json_data, content_type='application/json')