from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse_lazy


class UserProfileManager(models.Manager):
	use_for_related_fields =True

	def all(self):
		qs=self.get_queryset().all()
		try:
			if self.instance:
				qs=qs.exclude(user=self.instance)
		except:
			pass
		return qs

	def toggle_follow(self,user,to_toggle_user):
		user_profile, created = Profile.objects.get_or_create(user=user)
		if to_toggle_user in user_profile.following.all():
			user_profile.following.remove(to_toggle_user)
			added = False
		else:
			user_profile.following.add(to_toggle_user)
			added=True
			return added

	def is_following(self, user, followed_by_user):
		user_profile, created = Profile.objects.get_or_create(user=user)
		if created:
			return False
		if followed_by_user in user_profile.following.all():
			return True
		return False 

  

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    following=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name='followed_by')
    image=models.ImageField(default='default.png',upload_to='users/image')


    objects=UserProfileManager()


    def __str__(self):
        return str(self.following.all().count())


    def get_following(self):
    	users=self.following.all()
    	return users.exclude(username=self.user.username)


    def get_follow_url(self):
    	return reverse_lazy("follow", kwargs={"username":self.user.username})


    def get_absolute_url(self):
    	return reverse_lazy("user-posts", kwargs={"username":self.user.username})


