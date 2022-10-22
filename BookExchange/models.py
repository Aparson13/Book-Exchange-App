
from django.contrib.auth.models import User #add this


# Create your models here.
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib import admin
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
# 	pass

	


from django.contrib.auth.models import AbstractBaseUser,    BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
		username=username,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, username, password, **extra_fields):
    return self._create_user(email, username, password, False, False, **extra_fields)

  def create_superuser(self, email, username, password, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')

    self.username = username
    self.set_password(password)
    self.is_superuser = True
    self.is_staff = True
    self.active = True
    self.save(using=self._db)
    return self



class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=254, unique=True)
	name = models.CharField(max_length=254, null=True, blank=True)
	username = models.CharField(max_length=254, unique=True, default=name)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	last_login = models.DateTimeField(null=True, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'username'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	def get_absolute_url(self):
		return "/users/%i/" % (self.pk)

class Profile(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#OneToOne
	# @receiver(post_save, sender=User) #add this
	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Profile.objects.create(username=instance)

	# @receiver(post_save, sender=User) #add this
	# def create_profile(sender, instance, created, **kwargs):
	# 	user = instance
	# 	if created:
	# 		profile = Profile(username=user)
	# 		profile.save() 


	LOCATION_OPTIONS = (
 	("On", "On Grounds"),
 	("Off", "Off Grounds"),
 	)
	YEAR_OPTIONS = (
	("1", "1st year"),
	("2", "2nd year"),
 	("3", "3rd year"),
 	("4", "4th year"),
 	)
	year = models.CharField(max_length=15, choices=YEAR_OPTIONS, default=YEAR_OPTIONS[0][1])
	location = models.CharField(max_length=15, choices=LOCATION_OPTIONS, default=LOCATION_OPTIONS[0][1])
	last_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	major = models.CharField(max_length=200)

	def __str__(self):
		return str(self.user)

# Add Location (as multiple choice and make a default rating
	def __str__(self):
		return self.year

class ProfileForms(forms.ModelForm):
	class Meta:
			model = Profile
			fields = ['last_name', 'first_name', 'major', 'year', 'location']




# from django.db import models
# from django.forms import ModelForm
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=UserManager.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(email,
#             password=password
#         )

#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user



# class User(AbstractBaseUser):
#     objects = UserManager()
#     date_added = models.DateField(auto_now=False, auto_now_add=True)
#     email = models.EmailField(unique=True, db_index=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __unicode__(self):
#         return self.email

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     def get_full_name(self):
#     # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#     # The user is identified by their email address
#         return self.email

#     # On Python 3: def __str__(self):
#     def __unicode__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):

#     # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):

#     # Simplest possible answer: Yes, always
#         return True

#     def is_staff(self):

#     # Simplest possible answer: All admins are staff
#         return self.is_admin   