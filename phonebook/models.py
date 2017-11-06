from django.db import models

class contact(models.Model):
	contact_name = models.CharField(max_length = 20)
	number = models.CharField(max_length = 20)
	address = models.CharField(max_length = 20)

	def __str__(self):
		return self.contact_name
