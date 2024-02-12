from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def student_detail(request , id):
    student_obj= Student.objects.get(pk= id)
    serialize_data= StudentSerializer(student_obj)
    json_data= JSONRenderer().render(serialize_data.data)
    return HttpResponse( json_data, content_type='application/json')  

# querryset
def student_list(request):
    #complxe data
    student_obj= Student.objects.all()
    #complex data converted to python data or dic 
    serialize_data= StudentSerializer(student_obj, many=True)
    #dict type to json data
    json_data= JSONRenderer().render(serialize_data.data)
    return HttpResponse( json_data, content_type='application/json')  
    # common practice for non json type
    # return JsonResponse(serialize_data.data, safe=False)