from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)


# Abstract model Contact
class Contact(
	TimeStampedModel,  # Created/ Modified
	ActivatorModel,  # Activate/ Deactivate
	TitleDescriptionModel,  # Title/ Description
	Model  # Custom abstract model uses a UUID instead of the default ID
	):

	class Meta:
		verbose_name_plural = "Contacts"

	email = models.EmailField(verbose_name="Email")

	def __str__(self):
		return f'{self.title}'