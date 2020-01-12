from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# This import will be used for user permission
from django.contrib.auth.models import PermissionsMixin

# This is required to crearte a UserManager because we are overiding AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Helps django to work with our custom user model'''

    # Tell the django how to create a new user from a custom user model. We are telling without password we can create a user
    def create_user(self, email, name, password: None):
        '''Create a new user profile object.'''

        print('create_user method is invoked')
        # If email is not passed as argument
        if not email:
            raise ValueError('User must have an email address')

        # Standarize the email address to lowercase
        email = self.normalize_email(email)

        # Now create a user
        user = self.model(email=email, name=name)

        # We are using set_password because this method will encrypt the password that will be stored in database
        user.set_password(password)

        # Save the user into db
        user.save(using=self._db)

        # Finally return the user object that is just inserted in db
        return user

    # This method tell the django how to create a super user. password can not be None for super user
    def create_superuser(self, email, name, password):
        '''Create a new super user'''

        # First create  a standard user then convert it to super user
        user = self.create_user(email, name, password)

        # Convert normal user to super user
        user.is_superuser = True
        user.is_staff = True

        # Save the user into db
        user.save(using=self._db)

        # Finally return the user object that is just inserted in db
        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''This model will represent user profile in our system '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    # This field is required because we are overriding AbstractBaseUser
    is_staff = models.BooleanField(default=False)

    # Object manager is also required because we are overriding AbstractBaseUser.
    # It provide us functionality to create a admin user or just a regular user

    # We need to tell Django how to use our custom User model and this will be used to query all data objects.all()
    objects = UserProfileManager()

    # We are telling system we will login using email. By default email is required field
    USERNAME_FIELD = 'email'

    # All the field that are required. We can add more fields to this list.
    REQUIRED_FIELDS = ['name']

    # Add some helper functions
    def get_full_name(self):
        ''' Use to get users full name         '''

        return self.name

    def get_short_name(self):
        '''Use to get users short name'''

        return self.name

    # This method will let convert our object to String
    def __str__(self):
        '''This method will convert the object to String '''

        return self.email


class ProfileFeedItem(models.Model):
    """Update profile status"""
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text



