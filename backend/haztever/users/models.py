from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    
    username = None
    
    email = models.EmailField(_('email address '), unique=True)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email
    
    