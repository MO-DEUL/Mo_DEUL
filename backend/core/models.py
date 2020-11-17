from django.db import models


class TimeStampedModel(models.Model):

    """ 업로드 시간 기록 """

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
