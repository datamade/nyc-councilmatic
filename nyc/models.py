from django.db import models


class Person(models.Model):
	ocd_id = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	headshot = models.CharField(max_length=255, blank=True)
	# add districts

	def __str__(self):
		return self.name

class Bill(models.Model):
	ocd_id = models.CharField(max_length=100)
	name = models.TextField()
	classification = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=None)
	date_updated = models.DateTimeField(default=None, null=True)
	source_url = models.CharField(max_length=255)
	source_note = models.CharField(max_length=255, blank=True)
	from_organization = models.ForeignKey('Organization', related_name='bills', null=True)

	def __str__(self):
		return self.name

	@property
	def current_org(self):
		return self.actions.all().order_by('date').first().organization if self.actions.all() else None

class Organization(models.Model):
	ocd_id = models.CharField(max_length=100)
	name = models.CharField(max_length=255)
	classification = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.name

	@classmethod
	def committees(cls):
		return cls.objects.filter(classification='committee').order_by('name').all()

	@property
	def recent_activity(self):
		return self.actions.all() if self.actions.all() else None

class Action(models.Model):
	date = models.DateTimeField(default=None)
	classification = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	organization = models.ForeignKey('Organization', related_name='actions', null=True)
	bill = models.ForeignKey('Bill', related_name='actions', null=True)

class Post(models.Model):
	ocd_id = models.CharField(max_length=100)
	label = models.CharField(max_length=255)
	role = models.CharField(max_length=255)
	organization = models.ForeignKey('Organization', related_name='posts')

class Membership(models.Model):
	organization = models.ForeignKey('Organization', related_name='memberships')
	person = models.ForeignKey('Person', related_name='memberships')
	post = models.ForeignKey('Post', related_name='memberships', null=True)
	label = models.CharField(max_length=255, blank=True)
	role = models.CharField(max_length=255, blank=True)
	start_date = models.DateField(default=None, null=True)
	end_date = models.DateField(default=None, null=True)
