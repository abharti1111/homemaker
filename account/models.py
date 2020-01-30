from django.db import models
from django.contrib.auth.models import User
from .validators import validatePhoneNumber, ValidatePanId,ValidatePinCode
from django.conf import settings

# Create your models here.
# class Address(models.Model):
    # flatNo = models.CharField(max_length=20)
    # street = models.CharField(max_length=50)
    # landmark = models.CharField(max_length=50)
    # city = models.CharField(max_length=20)
    # district = models.CharField(max_length=20)
    # state = models.CharField(max_length=20)
    # pinCode = models.IntegerField(validators=[ValidatePinCode])

#     def __str__(self):
#         return self.flatNo + ', '+self.street

#     def get_Profile(self):
#         return Profile.objects.get(address=self)



USER_TYPE_CHOICES = (
    ("homemaker","homemaker"),
    ("customer","customer"),
    ("delivery","delivery"),
)
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("connected user"), on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(unique=True,validators=[validatePhoneNumber])
    profilePicture = models.ImageField(upload_to = 'accounts/images/' ,blank=True, null=True)
    userType = models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default="customer")
    # address = models.ManyToManyField(Address,blank=True,related_name='profiles',related_query_name='profile')
    flatNo = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinCode = models.IntegerField(validators=[ValidatePinCode])
    def __str__(self):
        return (self.user.username)

