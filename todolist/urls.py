from django.urls import path
from . import views

urlpatterns = [
	path('view/', views.view, name='view'),
	path('view/<int:id>/', views.list, name='list'),
	path('delList/', views.deleteList, name='delList'),
	path('signup/', views.signup, name='signup'),
	path('', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
]