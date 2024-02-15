from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
       json_data= request.body
       stream = io.BytesIO(json_data)
       python_data= JSONParser().parse(stream)
       serializer= StudentSerializer(data=python_data)
       if serializer.is_valid():
           serializer.save()
           res = {'msg': 'data created'}
           json_data= JsonResponse(res, safe=False)
        #    print(json_data)
           return HttpResponse( json_data, content_type='application/json')
       json_data=JSONRenderer.render(serializer.errors)
       return HttpResponse(json_data, content_type='application/json')