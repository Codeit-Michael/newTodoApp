from django.forms  import ModelForm
from .models import todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class todoForm(ModelForm):
	class Meta:
		model = todo
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']