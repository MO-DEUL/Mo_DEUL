from django.db import models
from core import models as core_models


class Community(core_models.TimeStampedModel):
    writer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Communities'


class Comment(core_models.TimeStampedModel):
    writer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey(
        'Community', on_delete=models.CASCADE, default=None)
    comment = models.TextField()

    def __str__(self):
        return self.comment
