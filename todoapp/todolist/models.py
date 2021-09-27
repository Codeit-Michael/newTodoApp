from django.db import models

# Create your models here.
class todo(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class item(models.Model):
	list = models.ForeignKey(todo, on_delete = models.CASCADE)
	text = models.CharField(max_length = 200)
	is_complete = models.BooleanField()

	def __str__(self):
		return self.name
