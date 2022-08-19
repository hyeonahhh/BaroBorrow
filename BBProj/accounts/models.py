
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, username, name, password=None):
        user = self.model(
            name = name,
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password=None):
        user = self.create_user(
            name = name,
            username = username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# 
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(default='', max_length=128, unique=True)
    nickname = models.CharField(default='', max_length=128, null=False, blank=False)
    name = models.CharField(default='', max_length=128, null=False, blank=False)
    location_city = models.CharField(default='null',max_length=64, null=True, blank=True)
    location_gu = models.CharField(default='null', max_length=64, null=True, blank=True)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    def get_full_name(self):       
        pass    
    def get_short_name(self):        
            pass    
    @property    
    def is_superuser(self):        
        return self.is_admin    
    @property    
    def is_staff(self):       
        return self.is_admin    
    def has_perm(self, perm, obj=None):       
        return self.is_admin    
    def has_module_perms(self, app_label):       
        return self.is_admin    
    @is_staff.setter    
    def is_staff(self, value):        
        self._is_staff = value
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.username


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#     # 일반 user 생성
#     def create_user(self, email, nickname, name, password=None):
#         if not email:
#             raise ValueError('must have user email')
#         if not nickname:
#             raise ValueError('must have user nickname')
#         if not name:
#             raise ValueError('must have user name')
#         user = self.model(
#             email = self.normalize_email(email),
#             nickname = nickname,
#             name = name
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
#     nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
#     name = models.CharField(default='', max_length=100, null=False, blank=False)
    
#     # User 모델의 필수 field
#     is_active = models.BooleanField(default=True)    
#     is_admin = models.BooleanField(default=False)
    
#     # 헬퍼 클래스 사용
#     objects = UserManager()

#     # 사용자의 username field는 nickname으로 설정
#     USERNAME_FIELD = 'nickname'
#     # 필수로 작성해야하는 field
#     REQUIRED_FIELDS = ['email', 'name']

#     def __str__(self):
#         return self.nickname