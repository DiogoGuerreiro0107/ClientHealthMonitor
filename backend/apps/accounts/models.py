from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

class AppUserRole(models.TextChoices):
    VIEWER = "V", _("Viewer")
    TECHNICIAN = "T", _("Technician")
    ADMIN = "A", _("Admin")

class AppUserManager(BaseUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a non-empty password")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password, commit=True, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", AppUserRole.VIEWER)
        if extra_fields["role"] not in AppUserRole.values:
            raise ValueError("User must have a valid user role")
        if extra_fields["is_staff"] or extra_fields["is_superuser"]:
            raise ValueError("User must not be staff or superuser")
        return self._create_user(email, password, commit, **extra_fields)

    def create_superuser(self, email, password, commit=True, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", AppUserRole.ADMIN)
        if not (extra_fields["is_staff"] and extra_fields["is_superuser"]):
            raise ValueError("A superuser must be both staff and superuser")
        if extra_fields["role"] not in AppUserRole.values:
            raise ValueError("User must have a valid user role")
        if extra_fields["role"] != AppUserRole.ADMIN:
            raise ValueError("A superuser must be an admin")
        return self._create_user(email, password, commit, **extra_fields)

    def get_user_by_email(self, email):
        if not email:
            raise ValueError("Must give an email")
        try:
            user = self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            raise ValueError("No user has the given email")
        return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=64, blank=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(
        max_length=1,
        choices=AppUserRole.choices,
        default=AppUserRole.VIEWER,
    )

    objects = AppUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
