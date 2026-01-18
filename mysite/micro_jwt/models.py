from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(60)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple'))
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'