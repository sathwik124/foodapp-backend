from django.db import models

# Create your models here.

class UserSignup(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)

class foods(models.Model):
    fid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pic = models.CharField(max_length=1000,default="x")
    price = models.IntegerField()
    tag = models.CharField(max_length=50)
    desc = models.CharField(max_length=10000)

class cartitems(models.Model):
    userid=models.ForeignKey(UserSignup, on_delete=models.CASCADE)
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    totprice = models.IntegerField()
    tag = models.CharField(max_length=1000)

class reviews(models.Model):
    rid = models.AutoField(primary_key=True)
    fid = models.ForeignKey(foods,on_delete=models.CASCADE)
    userid = models.ForeignKey(UserSignup, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    revdesc = models.CharField(max_length=10000,blank=True,null=True)
