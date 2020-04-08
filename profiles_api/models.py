from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#AbstractBaseUser, PermissionsMixin are used to override the default django user system

class UserProfileManager(BaseUserManager):
    #Create a new user profile
    def create_user(self, email, name, password=None):
        #Create a simple user
        if not email:
            raise ValueError("User should have an email address.")

        email = self.normalize_email(email) #First part of the email is case sensitive only
        user = self.model(email=email, name=name) #Creates a new model object

        user.set_password(password) #we use this to make the password be encrypted
        user.save(using=self._db) #we use self._db if we have multiple databases

        return user

    def create_superuser(self, email, name, password=None):
        #Create a super user
        user = self.create_user(email, name, password)

        user.is_superuser = True#built-in "is_superuser" variable
        user.is_staff = True #built-in "is_staff" variable
        user.save(using=self._db)

        return user

#######################################################################################################
#######################################################################################################

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Database model for users
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=28)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.name
