from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from apiapp.serializers import SignupSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apiapp.models import SignupDetails

# Create your views here.

@api_view(['GET'])
def firstApi(request):
    message='You have created an API'
    return Response(message)

@csrf_exempt
def signup(request, id = 0):
    if request.method == 'POST':
        userdata = JSONParser().parse(request)
        user_serializer = SignupSerializer(data = userdata)
              
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({'Status': 'Success', 'Data': user_serializer.data})
        return JsonResponse({'Status': 'Error'})

    elif request.method== 'GET':
        user = SignupDetails.objects.all()
        userSerializer = SignupSerializer(user, many=True)
        return JsonResponse(userSerializer.data, safe=False)

    elif request.method == 'PUT':
        userdata = JSONParser().parse(request)
        user = SignupDetails.objects.get(id = userdata['id'])
        user_serializer = SignupSerializer(user, userdata)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({"Status": "Success", "Data": user_serializer.data})
        else:
            return JsonResponse({"Status": "Failed", "Data": user_serializer.error})

    elif request.method == 'DELETE':
        print(id)
        user = SignupDetails.objects.get(id = id)
        user.delete()  
        return JsonResponse({"status": "Item deleted successfully"})


    



