from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to='profiles/', null=True, blank=True)
    mobile = models.CharField(max_length=100)
    photo_id = models.ImageField(verbose_name='Photo ID', upload_to='photo_ids', null=True, blank=True)
    is_scout = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    tokens = models.IntegerField(default=0)
    birth = models.DateField(default='2010-12-30')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Place(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    picture = models.FileField()
    uploader = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200)


class Travel(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField()


class Counter(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=100)
    photo = models.ImageField()
