from django.urls import path
from .import views

app_name='display'

urlpatterns=[
    path('',views.home,name="home")
]
