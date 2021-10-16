from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
# 	name = models.CharField(max_length=50, null=True)

	# def __str__(self):
	# 	return self.name

"""
	NOW I HOPE WE UNDERSTAND WHY WE NEED TO HAVE PROFILE MODEL W/ ONE TO ONE RELATION 
	THE USER. YOU SHOULD FINISH THIS SHIT BY TOMORROW...
"""

class todo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.title

class item(models.Model):
	list = models.ForeignKey(todo,null=True,on_delete=models.CASCADE)
	text = models.CharField(max_length=200,null=True)
	is_complete = models.BooleanField(null=True)

	def __str__(self):
		return self.text
