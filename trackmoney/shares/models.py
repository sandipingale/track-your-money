from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import request

# Create your models here.

txn_types = [("Buy", "Buy"),
            ("Sell", "Sell"),
            ("Div", "Div")
            ]

class Share(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    tnx_type = models.CharField(max_length=5, choices=txn_types)
    quantity = models.FloatField()
    txn_price = models.FloatField()
    txn_date = models.DateField()
    last_updated = models.DateTimeField(default=timezone.now)

