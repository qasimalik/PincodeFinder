from django.db import models

#Creating the required fields for the database
class PinCode_Fetcher(models.Model):
    id = models.IntegerField(primary_key=True)
    officename = models.CharField(max_length=200)
    pincode = models.IntegerField()
    officetype = models.CharField(max_length=50)
    deliverystatus = models.CharField(max_length=50)
    divisionname = models.CharField(max_length=100)
    regionname = models.CharField(max_length=100)
    circlename = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    districtname = models.CharField(max_length=100)
    statename = models.CharField(max_length=100)
    Relatedsuboffice = models.CharField(max_length=100)
    Relatedheadoffice = models.CharField(max_length=100)
    
    def __str__(self):
        return self.statename