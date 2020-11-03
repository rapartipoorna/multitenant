from django.db import models
from tenant_schemas.models import TenantMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneField
from django.conf import settings

# Create your models here.
class Client(TenantMixin):
    name=models.CharField(max_length=100)
    on_trial=models.BooleanField(default=False)
    first_tier = models.BooleanField(default=False)
    second_tier = models.BooleanField(default=False)
    third_tier= models.BooleanField(default=False)

    created_on=models.DateField(auto_now_add=True)
    auto_create_schema=True
    def __str__(self):
        return self.name


# manager for our custom model
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class
    """

    def create_user(self, email, username, phone,password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password,phone):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """
      Custom user class inheriting AbstractBaseUser class
    """

    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone=PhoneField(blank=True,help_text='contact phone number')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    # REQUIRED_FIELDS = ['username','phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
