from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save


class GolfUser(AbstractUser):

    email = models.EmailField(blank=False, unique=True)
    player_image = models.ImageField(default='default_image.jpg', upload_to='players_images/')
    height = models.IntegerField(null=True, validators=[MinValueValidator(100), MaxValueValidator(250)])
    handicap = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(36)])
    sensor_id = models.CharField(unique=True, max_length=25, default="")

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


@receiver(pre_save, sender=GolfUser)
def fill_username(sender, instance, **kwargs):
    instance.username = instance.first_name + ' ' + instance.last_name
