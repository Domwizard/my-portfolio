import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Project, Profile

#Проект

@receiver(pre_save, sender=Project)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return False
    new_file = instance.photo
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(post_delete, sender=Project)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

#Профиль

@receiver(pre_save, sender=Profile)
def delete_old_profile_photo_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    new_file = instance.image
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(post_delete, sender=Profile)
def delete_profile_photo_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)