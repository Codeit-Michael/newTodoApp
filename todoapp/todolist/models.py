from django.db import models

# Create your models here.
class todo(models.Model):
	name = models.CharField(max_length = 50, null=True)

	def __str__(self):
		return self.name

class item(models.Model):
	list = models.ForeignKey(todo,null=True,on_delete=models.CASCADE)
	text = models.CharField(max_length=200,null=True)
	is_complete = models.BooleanField(null=True)

	def __str__(self):
		return self.text
