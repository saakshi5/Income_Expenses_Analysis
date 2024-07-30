from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='expenses'),
     path('income/', views.income, name='income'),
     path('expenses/', views.stats, name='stats'),
     path('preferences/', views.preferences, name='preferences'),
    path('add_expense',views.add_expense,name='add_expense')
]