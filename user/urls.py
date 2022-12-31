from django.urls import path
from . import views
urlpatterns = [
    path('',views.helloworld),
    path('hello/<int:number>',views.helloworld),
    path('store_person',views.store_person,name='store_person')
]