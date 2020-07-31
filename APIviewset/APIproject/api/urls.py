from .views import Staff_List,Staff_Detail
from django.urls import path
urlpatterns = [
    path('staff-list/',Staff_List,name='stafflist'),
    path('staff-detial/<int:pk>',Staff_Detail,name='staffdetail'),
]