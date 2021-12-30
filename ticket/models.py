from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Type(models.Model):
    TYPE_CHOICES = (
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Testing', 'Testing'),
    )
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)

    def __str__(self):
        return self.type


def hex_uuid():
    return uuid.uuid4().hex


class Ticket(models.Model):
    user_name = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    ticket_no = models.CharField(default=hex_uuid, max_length=50, editable=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    prior = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Response(models.Model):
    REPLY = (
        ('Un-reviewed', 'Un reviewed'),
        ('Accepted', 'Accepted'),
        ('In-process', 'Ready for checking'),
        ('Solved', 'Solved'),
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    reply = models.CharField(max_length=15, choices=REPLY, default='Un-reviewed')
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.reply)
