# models.py
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


class Company(models.Model):
    name = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    registration_number = EncryptedCharField(max_length=50)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = EncryptedCharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)


class RoleHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()
