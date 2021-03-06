from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Company(models.Model):
    name = models.CharField(
        max_length=70
    )

    def __str__(self):
        return self.name


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='profiles'
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    description = models.CharField(
        max_length=100,
        blank=True
    )


class Facility(models.Model):
    name = models.CharField(
        'Facility Name',
        max_length=70
    )
    location = models.CharField(
        max_length=150,
        blank=True
    )
    owner = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='facilities'
    )
    facility = models.ForeignKey(
        'FacilityManager',
        on_delete=models.CASCADE,
        related_name='managers'
    )


class FacilityManager(models.Model):
    name = models.CharField(
        'Manage Name',
        max_length=70
    )
    address = models.CharField(
        max_length=150,
        blank=True
    )
    phone = models.IntegerField(
        blank=True,
        null=True
    )


class Apartment(models.Model):
    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name='apartments'
    )
    number = models.IntegerField(
        'Apartment Number',
        blank=True,
        null=True
    )


class Tenant(models.Model):
    first_name = models.CharField(
        max_length=70
    )
    last_name = models.CharField(
        max_length=70
    )
    email = models.EmailField(
        max_length=70
    )
    apartment = models.OneToOneField(
        Apartment,
        on_delete=models.CASCADE
    )


class Request(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='comp_requests'
    )
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name='requests'
    ),
    description = models.CharField(
        max_length=200,
        blank=True
    )
