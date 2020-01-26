from django.db import models
from account.models import Profile
from account.validators import ValidatePanId
from django.core.validators import URLValidator

# Create your models here.
class Organisation(models.Model):
    owner = models.OneToOneField(Profile,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    panId = models.CharField(max_length=10,validators=[ValidatePanId],unique=True)
    description = models.CharField(max_length=255)
    weeklyPrice = models.IntegerField(default=500)
    isVeg = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.FloatField()
    picture = models.ImageField(upload_to='media/organisation/images/',blank=True,null=True)
    extra_stock = models.PositiveIntegerField(default=0)
    facebook_page = models.URLField(validators=[URLValidator], null=True, blank=True,max_length=200)
    instagram_page = models.URLField(validators=[URLValidator], null=True, blank=True,max_length=200)
    updated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

class Menu(models.Model):
    org = models.OneToOneField(Organisation,on_delete=models.CASCADE,null=True)
    sunday = models.TextField(blank=True,null=True)
    monday = models.TextField(blank=True,null=True)
    tuesday = models.TextField(blank=True,null=True)
    wednesday = models.TextField(blank=True,null=True)
    thursday = models.TextField(blank=True,null=True)
    friday = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.org)


