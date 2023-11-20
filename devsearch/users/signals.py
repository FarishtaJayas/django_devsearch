from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        user = instance
        user = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


def updateUser(sender, instance, created, *args, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteProfile(sender, instance, *args, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)


# @receiver(post_save, sender=Profile)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile Save!')
#     print('Instance:', instance)
#     print('created', created)


# @receiver(post_delete)
# def deleteUser(sender, instance, **kwargs):
#     print('Deleting User')


# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)
