from django.urls import path
from Core import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup')
]
