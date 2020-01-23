from django.db import models
from account.models import Profile
from django.utils import timezone
import datetime

# Create your models here.

class Booking(models.Model):
    subscriber = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='subscriber')
    subscribedTo = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='subscribed_to')
    startDate = models.DateField(default=timezone.now)
    EndDate = models.DateField(default=datetime.date.today()+datetime.timedelta(weeks=1))
    weeks = models.IntegerField(default=1)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.subscribedTo.user.username




