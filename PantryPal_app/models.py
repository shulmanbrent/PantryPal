from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Query(models.Model):
	id = models.IntegerField(primary_key=True)
	user =  models.CharField(max_length=30)
	query = models.CharField(max_length=200)

	def __unicode__():
		return self.user + ": " + query
