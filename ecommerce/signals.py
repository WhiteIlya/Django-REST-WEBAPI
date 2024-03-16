from django.db.models.signals import post_save  # After something posted we receive a signal
from django.dispatch import receiver  # Receiver to receive a signal
from django.contrib.auth.models import User  # Core/User table
from rest_framework.authtoken.models import Token  # We want to create a token

'''
We want to create a token every time a user creates in a DB. To do that,
we create a signal - piece of code which receives a signal from a certain table
When a certain instance created in database it sends a signal and we catch it
as an antenna with a receiver

It is necessary to wire the app => When the app starts it is starting looking for a signal
'''

@receiver(post_save, sender=User, weak=False)
def report_uploaded(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)