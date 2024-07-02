from django.db import models
import uuid
from encrypted_model_fields.fields import EncryptedCharField
from django.core.validators import RegexValidator, EmailValidator


class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    registration_date = models.DateField()
    registration_number = EncryptedCharField(max_length=50)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])
    email = models.EmailField(max_length=255, validators=[EmailValidator()])

    class Meta:
        ordering = ['name']


class Department(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        ordering = ['name']


class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    employee_id = EncryptedCharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']


class RoleHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()

    def __str__(self):
        return self.employee.name

    class Meta:
        ordering = ['-date_started']
