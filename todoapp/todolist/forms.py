from django.forms  import ModelForm
from .models import todo #,profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class todoForm(ModelForm):
	class Meta:
		model = todo
		fields = ['title']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']

# class profileForm(ModelForm):
# 	class Meta:
# 		model = profile
# 		fields = '__all__'