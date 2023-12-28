from django.urls import path
from . import views

urlpatterns=[
    path('<int:id>',views.list, name='list'),
    path('',views.homePage, name='homePage'),
    path('createNewList/',views.createNewList, name='creteNewList'),
    path('view/',views.view, name='view'),
]