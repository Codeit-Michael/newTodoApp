from django.forms  import ModelForm
from .models import Todo #,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['title']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']

# class profileForm(ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = '__all__'