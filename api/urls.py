from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers
 
#Step 5 : creating the urls

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]

 