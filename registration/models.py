from django.db import models
from django.contrib.auth.models import User,auth
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField, get_thumbnail
import datetime
from datetime import datetime
# Create your models here.


class extendedUser(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    username    = models.CharField(max_length=30)
    phone       = models.CharField(max_length=12)
    dateofbirth = models.DateField(blank=True, null=True)
    profile     = models.ImageField(upload_to ='profile')
    userType    = models.CharField(max_length=20)
    token       = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        if self.profile:
            self.profile = get_thumbnail(self.profile, '500x600', quality=99, format='JPEG').url
        super(extendedUser, self).save(*args, **kwargs)


    @property
    def age(self):
        return int((datetime.now().date() - self.dateofbirth).days / 365.25)
