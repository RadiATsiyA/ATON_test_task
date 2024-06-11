from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Client(models.Model):
    STATUS_CHOICES = [
        ('not_in_work', 'Не в работе'),
        ('in_work', 'В работе'),
        ('rejected', 'Отказ'),
        ('deal_closed', 'Сделка закрыта'),
    ]

    account_number = models.IntegerField(unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    inn = models.CharField(max_length=50, unique=True)
    responsible_full_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='not_in_work')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
