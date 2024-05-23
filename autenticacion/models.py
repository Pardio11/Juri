from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user (self, email, username, password=12345678):
        if not email:
            raise ValueError("El correo es requerido")
        if not username:
            raise ValueError("El usuario es requerido")
        user= self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save()

        return user
    def create_superuser (self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email= models.EmailField(max_length=60, unique=True)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=('username',)

    objects = AccountManager()
    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.username
