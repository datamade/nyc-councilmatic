from django.db import models


class Person(models.Model):
	ocd_id = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	headshot = models.CharField(max_length=255, blank=True)
	# add districts

class Committee(models.Model):
	name = models.CharField(max_length=100)

class Bill(models.Model):
	ocd_id = models.CharField(max_length=100)
	name = models.CharField(max_length=255)
	classification = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=None)
	date_updated = models.DateTimeField(default=None, null=True)
	source_url = models.CharField(max_length=255)
	source_note = models.CharField(max_length=255, blank=True)
