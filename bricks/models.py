from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.cache import cache
from django.conf import settings


def natural_key(self):
	return ({'username': self.username, 'email': self.email, 'first_name': self.first_name, 'last_name': self.last_name})

User.add_to_class("natural_key", natural_key)


class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zip = models.PositiveIntegerField(default=0)
	phone = models.CharField(max_length=10)
	post_count = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.user.first_name






#To keep user and userinfo tables in sync
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userinfo.save()