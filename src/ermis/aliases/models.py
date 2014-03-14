from django.db import models

class Alias(models.Model):
	alias_name = models.CharField(max_length=40,unique=True)
	type = models.CharField(max_length=15)
	
	def __str__(self):
		return "Alias name %s, type %s" % (self.alias_name, self.type)


