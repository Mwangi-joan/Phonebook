from django.urls import path
from . import views

app_name= 'app'

urlpatterns = [
path('',views.ContactListView.as_view(), name='index'),
path('add_contact',views.ContactCreateView.as_view(), name='add_contact'),
path('(?P<name_id>[0-9]+)/delete', views.delete_contact, name='delete_contact'),
path('(?P<name_id>[0-9]+)/update', views.update_contact, name='update_contact'),
path('login', views.login_user, name='login'),

]