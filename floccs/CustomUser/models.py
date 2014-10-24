from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.core.urlresolvers import reverse



class UserManager(BaseUserManager):

    def _create_user(self, username, email,  password, 
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email, password, first_name, last_name and place_of_stay.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None,  **extra_fields):
        return self._create_user( username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username,  email, password, **extra_fields):
        return self._create_user(username, email,password, True, True,
                                 **extra_fields)



class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """
    username= models.CharField(_("username"), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank = False)

    

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    place_of_stay = models.CharField(max_length=150, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    #has_active_event = models.BooleanField(default=False)
   



    def get_absolute_url(self):
       
        ''' for viewing one's own profile'''

        return reverse('profile', kwargs={'username': self.username})

    def view_profile(self):
       
        ''' for viewing other's profile'''

        return reverse('view_profile', kwargs={'username': self.username })



    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'







admin.site.register(User)
