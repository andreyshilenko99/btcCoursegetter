from django.urls import path
from getter import views
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('last/', views.get_last),
    path('all/', views.get_all)
]