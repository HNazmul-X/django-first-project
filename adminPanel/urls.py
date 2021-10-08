from django.urls import path
from adminPanel import views

urlpatterns = [
    path("",views.adminIndex,name="adminPanel")
]
