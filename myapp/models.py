#from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class lessonplanBatch(models.Model):
    batch=models.CharField(max_length=20)
    academicyear=models.CharField(max_length=20)
    programme=models.CharField(max_length=20)
    semester=models.CharField(max_length=20)
    section=models.CharField(max_length=10)
    name_of_the_course=models.CharField(max_length=70)
    course_code=models.CharField(max_length=15)
    def __str__(self):
        return self.course_code
class courseoutcomes(models.Model):
    co=models.CharField(max_length=5,default='1')
    courseoutcome=models.CharField(max_length=100)
    knowledge_level=models.CharField(max_length=5,default='K1')
    course_code=models.CharField(max_length=15)
class textbooks(models.Model):
    sno=models.CharField(max_length=5,default=1)
    textbook_details=models.CharField(max_length=200)
    course_code=models.CharField(max_length=15)
class referencebooks(models.Model):
    sno=models.CharField(max_length=5,default='1')
    rfbook_details=models.CharField(max_length=200)
    course_code=models.CharField(max_length=15)
class targetproficiency(models.Model):
    co=models.CharField(max_length=15,default='')
    tpl=models.CharField(max_length=15,default='')
    l3=models.CharField(max_length=15,default='')
    l2=models.CharField(max_length=15,default='')
    l1=models.CharField(max_length=15,default='')
    #tpl=models.CharField(max_length=50,default="Target Proficiency Level")
    course_code=models.CharField(max_length=15)
class lectureplan(models.Model):
    sno=models.CharField(max_length=5,default='1')
    course_outcome=models.CharField(max_length=10,default='CO1')
    ilo=models.CharField(max_length=100,default='')
    knowledgelevel=models.CharField(max_length=5,default='')
    noof_hours=models.CharField(max_length=5,default='')
    pedagogy=models.CharField(max_length=50,default='')
    teachingaids=models.CharField(max_length=10,default='')
    course_code=models.CharField(max_length=15)
class co_pso_Matrix(models.Model):
    cos=models.CharField(max_length=10,default='')
    po1=models.CharField(max_length=10,default='')
    po2=models.CharField(max_length=10,default='')
    po3=models.CharField(max_length=10,default='')
    po4=models.CharField(max_length=10,default='')
    po5=models.CharField(max_length=10,default='')
    po6=models.CharField(max_length=10,default='')
    po7=models.CharField(max_length=10,default='')
    po8=models.CharField(max_length=10,default='')
    po9=models.CharField(max_length=10,default='')
    po10=models.CharField(max_length=10,default='')
    po11=models.CharField(max_length=10,default='')
    po12=models.CharField(max_length=10,default='')
    pso1=models.CharField(max_length=10,default='')
    pso2=models.CharField(max_length=10,default='')
    course_code=models.CharField(max_length=15)
class course_end_survey(models.Model):
    sno=models.CharField(max_length=5,default='1')
    cos=models.CharField(max_length=5,default='')
    question=models.CharField(max_length=100,default='')
    course_code=models.CharField(max_length=15)
class details_of_instructors(models.Model):
    sno=models.CharField(max_length=5,default='1')
    name=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')
    year=models.CharField(max_length=20,default='')
    section=models.CharField(max_length=20,default='')
    contactno=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=50,default='')
    course_code=models.CharField(max_length=15)
class teachers(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=80,default='sushma kurella')
    passwd=models.CharField(max_length=50)
    def __str__(self):
        return self.name
# appname/models.py

# from django.db import models


# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username

#just commented
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'  # Change to 'email' if needed
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username

#just commented