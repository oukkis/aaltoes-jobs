from django.db import models

class Employee(models.model):
	first_name = models.Charfield(max_length=30)
	last_name = models.Charfield(max_length=30)
	date_of_birth = models.Datefield()
	phone_number = models.Integerfield()
	email = models.EmailField(max_length=254)
	password = models.Charfield()
	description = models.Charfield(max_length=1000)

class Employer(models.model):
	company_name = models.Charfield(max_length=100)
	contact_info = models.Charfield(max_length=100)
	phone_number = models.Integerfield()
	email = models.EmailField(max_lenght=254)
	password = models.Charfield()

class Job(models.model):
	employer = models.Foreigkey('Employer')
	description = models.Charfield(max_length=1000)
	contact_info = models.Charfield(max_length=100)
	date_field = Datefield.auto_now
	expire_date = models.Datedfield()








