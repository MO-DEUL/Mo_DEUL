from django.contrib.auth.models import AbstractUser
from django.db import models


class SocialPlatform(models.Model):
    platform = models.CharField(max_length=20, default=0)

    class Meta:
        db_table = "social_platform"


class User(AbstractUser):

    GENDER_MALE = "남성"
    GENDER_FEMALE = "여성"
    GENDER_OTHERS = "기타"

    GENDER_CHOICES = (
        (GENDER_MALE, "남성"),
        (GENDER_FEMALE, "여성"),
        (GENDER_OTHERS, "기타"),
    )

    LANGUAGE_EN = "en"
    LANGUAGE_KR = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_EN, "English"),
        (LANGUAGE_KR, "한국어"),
    )

    STATUS_HOST = "호스트"
    STATUS_GUEST = "게스트"

    STATUS_CHOICES = (
        (STATUS_HOST, "호스트"),
        (STATUS_GUEST, "게스트"),
    )

    social = models.ForeignKey(
        SocialPlatform, on_delete=models.CASCADE, max_length=20, blank=True, default=1)
    social_login_id = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, blank=False, default="")
    superhost = models.BooleanField(default=False)
