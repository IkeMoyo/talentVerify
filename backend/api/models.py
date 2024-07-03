from django.db import models
import uuid
from encrypted_model_fields.fields import EncryptedCharField
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    registration_date = models.DateField()
    registration_number = EncryptedCharField(max_length=50)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
            )
        ]
    )
    email = models.EmailField(
        max_length=255,
        validators=[EmailValidator(message=_("Enter a valid email address."))]
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]


class Department(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]


class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    employee_id = EncryptedCharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class RoleHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()

    def __str__(self):
        return f'{self.employee.name} - {self.role}'

    def clean(self):
        if self.date_left and self.date_started and self.date_left < self.date_started:
            raise ValidationError(_('Date left cannot be before date started.'))

    class Meta:
        ordering = ['-date_started']
        indexes = [
            models.Index(fields=['employee', 'company', 'department']),
        ]
