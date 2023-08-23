
from django.urls import path
from .views import pay, success

urlpatterns = [
    path('', pay, name='pay'),
     path('success/' , success , name='success')
]
