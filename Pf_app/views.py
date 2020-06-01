from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PinCode_Fetcher
from .serializers import PincodeSerializer

#Rendering the index.html file for client
def index(request):
    return render(request, 'index.html')

#Viewing the dataset as other formats(json)
class Pincode_list(APIView):

    def get(self, request):
        Pincode1 = PinCode_Fetcher.objects.all()
        serializer = PincodeSerializer(Pincode1, many=True)
        return Response(serializer.data)

    def post(request):
        pass