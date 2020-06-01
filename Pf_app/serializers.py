from rest_framework import serializers
from .models import PinCode_Fetcher

#Creating serializer to convert the dataset to format
class PincodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PinCode_Fetcher
        fields = '__all__'                                     #fetching all the fields
