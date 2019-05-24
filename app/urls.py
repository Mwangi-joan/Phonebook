from django.urls import path
from . import views

app_name= 'app'

urlpatterns = [
path('',views.ContactListView.as_view(), name='index'),
path('add_contact',views.ContactCreateView.as_view(), name='add_contact'),
]