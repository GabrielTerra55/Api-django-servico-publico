from django.db import models

class Pessoas(model.Model):
	
	name = models.CharField(max_lenght=30)
	birth = models.DateField(blank=False)
	e_mail = models.EmailField(max_length=250)
	state = 
	

