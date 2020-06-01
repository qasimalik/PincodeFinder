from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Pf_app import views

urlpatterns = [
    path('index/', views.index),                                        #Calling the index.html
    path('admin/', admin.site.urls),                                    #Caliing the default admin page
    path('pincode/', views.Pincode_list.as_view()),                     #Calling the APIView model
]
