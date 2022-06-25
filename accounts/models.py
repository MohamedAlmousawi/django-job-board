from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True,blank=True)
    phone= models.CharField(max_length = 15)
    image = models.ImageField(upload_to='profile/')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)