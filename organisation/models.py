from django.db import models
from account.models import Profile
from account.validators import ValidatePanId

# Create your models here.
class Menu(models.Model):
    sunday = models.TextField(blank=True,null=True)
    monday = models.TextField(blank=True,null=True)
    tuesday = models.TextField(blank=True,null=True)
    wednesday = models.TextField(blank=True,null=True)
    thursday = models.TextField(blank=True,null=True)
    friday = models.TextField(blank=True,null=True)

    def __str__(self):
        # print(type(self.organisations))
        return str(self.pk)

class Organisation(models.Model):
    owner = models.OneToOneField(Profile,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    panId = models.CharField(max_length=10,validators=[ValidatePanId],unique=True)
    description = models.CharField(max_length=255)
    weeklyPrice = models.IntegerField(default=500)
    isVeg = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.FloatField()
    picture = models.ImageField(upload_to='statics/organisation/images/',blank=True,null=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,related_name='organisations',related_query_name='organisation')

    def __str__(self):
        return self.name

