from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from hrms_api.choices import GenderTypeChoice, MaritalStatusChoice


class Department(models.Model):
    department_name = models.CharField(verbose_name='Department Name', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.department_name


class Designation(models.Model):
    designation_name = models.CharField(verbose_name='Designation Name', max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.designation_name


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):

        if "phone" in kwargs and 'password' in kwargs:
            phone = kwargs.pop("phone")
            password = kwargs.pop("password")
            user = self.model(
                phone=phone,
                **kwargs)
            user.set_password(password)
        elif "phone" in kwargs:
            phone = kwargs.pop("phone")
            user = self.model(
                phone=phone,
                **kwargs)
        else:
            raise ValueError('Users must have an phone and password')

        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        user = self.create_user(
            phone=phone,
            **kwargs
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(verbose_name='User Name', max_length=255, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number entered in format +910987654321 .")
    country_code = models.IntegerField(blank=True, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    dob = models.DateField(verbose_name='Birth Date', null=True, blank=True)
    address = models.CharField(verbose_name='Address', max_length=400, blank=True, null=True)
    nationality = models.CharField(verbose_name='Nationality', max_length=255, blank=True)
    email = models.EmailField(verbose_name='Email Address', max_length=255, blank=False)
    gender = models.CharField(verbose_name='Gender', choices=GenderTypeChoice.choices, default='', max_length=255, null=True)
    report_to = models.CharField(verbose_name='Report to', blank=True, null=True, max_length=255)
    is_admin = models.BooleanField(verbose_name='is admin', default=False, blank=True)
    is_staff = models.BooleanField(verbose_name='is staff', default=False, blank=True)
    avatar = models.ImageField(verbose_name='Profile Image', upload_to='avatars', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank=True)
    date_joined = models.DateField(verbose_name='Date of Joining', null=True, blank=True)
    birthdate = models.DateField(verbose_name='Birth Date', null=True, blank=True)
    marital_status = models.CharField(verbose_name='Marital Status', choices=MaritalStatusChoice.choices, default='', null=True, max_length=255)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username


class Holiday(models.Model):
    holiday_title = models.CharField(verbose_name='Holiday Title', max_length=255, null=True, blank=True)
    holiday_date = models.DateField(verbose_name="Holiday Date", null=True, blank=True)

    def __str__(self):
        return self.holiday_title
