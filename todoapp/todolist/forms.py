from django.forms  import ModelForm
from .models import todo

class todoForm(ModelForm):
	class Meta:
		model = todo
		fields = '__all__'