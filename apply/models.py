from django.db import models
from core import models as core_models


class Apply(core_models.TimeStampedModel):
    name = models.CharField(max_length=100)
    house = models.ForeignKey(
        'houses.House', on_delete=models.CASCADE, null=True)
    guest = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Applies"
