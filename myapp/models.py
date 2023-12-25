from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    wallet = models.IntegerField()


class Goods(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

class Purchase(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)
    client = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    purchase_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class ReturnGoods(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)