from django.db import models

class Category(models.Model):
	"""This is the model for the categories that will be stored in the 
	Rango app"""
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	class Meta:
		verbose_name_plural = 'categories'
		
	def __str__(self):
		return self.name

class Page(models.Model):
	"""This is the model for the pages that will belong that at least one 
	category and will be shown in the Rango app"""
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title
		
		