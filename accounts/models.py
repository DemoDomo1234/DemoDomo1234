from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, username, body, image,
     gender, address, last_name, frest_name, password=None , is_admin=False,
      is_staff=False, is_active=True , is_superuser = True):
        if not username:
            raise ValueError('Users must have an username address')
        else:
            email=self.normalize_email(email),
            user = self.model(username = username, body = body, image = image, gender = gender, address = address, last_name = last_name, frest_name = frest_name, date_of_birth = date_of_birth)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email , date_of_birth , username , body ,
     image , gender , address , last_name , frest_name , password = None ):
        user = self.create_user(username=username , email=email , body=body , image=image , gender=gender , address=address , last_name=last_name , frest_name=frest_name , date_of_birth=date_of_birth , password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class account(AbstractBaseUser):
    username = models.CharField(max_length=200 , unique=True)
    last_name = models.CharField(max_length=200 , null=True , blank=True)
    frest_name = models.CharField(max_length=200 , null=True , blank=True)
    email = models.EmailField(max_length=254 , null=True , blank=True)
    address = models.TextField(null=True , blank=True)
    body = models.TextField(null=True , blank= True)
    image = models.ImageField(upload_to='mdia' , null=True , blank= True)
    gender = models.BooleanField(null=True , blank=True)
    date_of_birth = models.DateField()
    folower = models.ManyToManyField("self", related_name='folo', blank = True , symmetrical = False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateField(null=True , blank=True)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth' , 'email' , 'image' , 'body' , 'address' , 'gender' , 'last_name' , 'frest_name']

    def __str__(self):
        return self.username
        
    def get_absolute_url(self):
        return reverse("accounts:home")

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

