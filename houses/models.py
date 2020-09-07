from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HouseType(AbstractItem):
    pass


class House(core_models.TimeStampedModel):

    name = models.CharField(max_length=140)
    description = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    house_type = models.ManyToManyField(HouseType, blank=True)
    host = models.ForeignKey(
        "users.User", related_name="houses", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
