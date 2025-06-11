from django.urls import path
from .views import *     

urlpatterns = [
    path('delete/<int:id>/',delete,name="delete"),
    path('create_p/',create,name="create"),    
    path('update/<int:id>/',update,name="update"),
    path('rendeer/',rendeer,name="rendeer"),
    path('update_data/<int:id>/',update_data,name="update_data"),
    path('delete_data/<int:id>/',delete_data,name="delete_data"),
    path("get_user/", get_user, name="get_user"),
    
    path('create_phone/',create_phone,name="create_phone"),
    path('rendeer_phone/',rendeer_phone,name="rendeer_phone"),
    path('update_phone/<int:id>/',update_phone,name="update_phone"),
    path('delete_phone/<int:id>/',delete_phone,name="delete_phone"),   
]
