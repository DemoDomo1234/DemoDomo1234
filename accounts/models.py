from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipTo
from uuid import uuid4


class UserManager(BaseUserManager):
    def create_user(self, email, name, body, image, password=None,
                    is_admin=False, is_staff=False, is_active=False,
                    is_superuser=False):
        
        if not email:
            raise ValueError('Users must have an email address')
        else:
            user = self.model(email=self.normalize_email(email))            
            user=self.model(email=email, name=name,
                            body=body, image=image)
            
            user.set_password(password)
            user.save(using=self._db)

            return user
            

    def create_superuser(self, email, body,
                        image, name, password=None):
        
        user = self.create_user(name=name, email=email, body=body,
                                image=image, password=password)
        
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='user_image',
                            null=True, blank=True)
    follower = models.ManyToManyField("self", related_name='follow',
                                    blank=True, symmetrical=False)
    notifications =  models.ManyToManyField("self", related_name='user_notification',
                                            blank=True, symmetrical=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateField(null=True, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['image', 'body', 'name']

    def __str__(self):
        return self.email
        
    def get_absolute_url(self):
        return reverse("accounts:Profile", args=[self.id])

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Following(StructuredNode):
    code = StringProperty(unique_index=True, default=uuid4)
    name = StringProperty()
    user_id = StringProperty(index=True)
    followers = RelationshipTo('Following', 'FOLLOWER')


class OTPCode(models.Model):
    user = models.ForeignKey(User, related_name='user_otp', on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    created = models.DateTimeField(auto_now_add=True)

    