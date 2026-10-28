from django.db import models
from django.db.models import Q
import django.core.validators


class Customer(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    phone_regex = django.core.validators.RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, unique=True, validators=[phone_regex])

    def __str__(self):
        return self.full_name


class Address(models.Model):
    category_choices = (
        ('HOME', 'home'),
        ('WORK', 'work'),
        ('OTHER', 'other'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField(
        validators=[
            django.core.validators.MinValueValidator(10000),
            django.core.validators.MaxValueValidator(9999999999)
        ]
    )
    landmark = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=category_choices, default='OTHER')
    is_primary = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['customer'], condition=Q(is_primary=True), name='unique_customer'),
        ]
        indexes = [
            models.Index(fields = ['city','pincode'])
        ]