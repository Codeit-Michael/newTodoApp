from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
# 	name = models.CharField(max_length=50, null=True)

# 	def __str__(self):
# 		return self.name

class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)	
	title = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.title

class Item(models.Model):
	todo = models.ForeignKey(Todo,null=True,on_delete=models.CASCADE)
	text = models.CharField(max_length=200,null=True)
	is_complete = models.BooleanField(null=True)

	def __str__(self):
		return self.text
