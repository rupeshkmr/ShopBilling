from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
