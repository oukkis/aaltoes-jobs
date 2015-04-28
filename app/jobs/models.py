from django.db import models

class Employee(models.model):
	first_name = models.Charfield(max_length=30)
	last_name = models.Charfield(max_length=30)
	picture = models.
	date_of_birth = models.Datefield()
	phone_number = models.Integerfield()
	email = models.EmailField(max_length=254)
	password = models.Charfield()
	description = models.Charfield(max_length=1000)
	linkedin = models.URLfield(max_length=100)

class Employer(models.model):
	company_name = models.Charfield(max_length=100)
	password = models.Charfield()
	logo = models.

class Job(models.model):
	employer = models.Foreigkey('Employer')
	description = models.Charfield(max_length=1000)
	contact_info = models.Charfield(max_length=100)
	phone_number = models.Integerfield()
	email = models.EmailField(max_lenght=254)
	date_field = Datefield.auto_now
	expire_date = models.Datedfield()

class PreviousJob(models.model):
	company_name = models.Charfield(max_length=100)
	job_title = models.Charfield(max_length=30)
	job_description = models.Charfield(max_length=200)
	job_start = Datefield.
	job_end = Datefield.

class Studies(models.model):
	school_name = models.Charfield(max_length=50)
	degree = models.Charfield(max_legth=100, choices=DEGREE_CHOICES, blank=False, null=False)
	school_start = models.Datefield
	school_end = models.Datefield

DEGREE_CHOICES = (
	("amis")
	("uliulioppilas")
	("teekkarijäbä")

	)








