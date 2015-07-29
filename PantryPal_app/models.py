from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Query(models.Model):
	id = models.IntegerField(primary_key=True)
	user =  models.CharField(max_length=30)
	user_email = models.CharField(max_length=75)
	query = models.CharField(max_length=256)

	def __unicode__(self):
		return self.user + ": " + self.query
