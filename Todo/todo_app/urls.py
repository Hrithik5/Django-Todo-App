
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main),
    path('add/',views.add, name="add"),
    path('delete/<int:todo_id>/',views.deleteItem, name="delete"),
    
] 