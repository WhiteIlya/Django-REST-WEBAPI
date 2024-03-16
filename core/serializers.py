from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField


class ContactSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)  # We want this field be named "name" instead of title
    message = CharField(source="description", required=True)  # The same
    email = EmailField(required=True)

    class Meta:
        model = models.Contact
        fields = (
            'name',
            'email',
            'message'
        )