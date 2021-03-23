from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# We want to create profile on user creation

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if instance and created:
        profile = Profile.objects.create(user=instance) # profile image has default image
        profile.save()

        #Alternative
        # isntance.profile = Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

