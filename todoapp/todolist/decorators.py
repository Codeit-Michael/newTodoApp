from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(views_func):
	def wrapper_func(request, *args, **kwargs):
			if request.user.is_authenticated:
				return redirect('view')
			else:
				return views_func(request, *args, **kwargs)
	return wrapper_func