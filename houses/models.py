from django.db import models
from django.urls import reverse
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)
    subtitle = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HouseType(AbstractItem):

    class Meta:
        verbose_name = "House Type"


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilities"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="house_photos")
    house = models.ForeignKey("House", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class House(core_models.TimeStampedModel):

    name = models.CharField(max_length=140)
    description = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    house_type = models.ForeignKey(
        HouseType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilites = models.ManyToManyField(Facility, blank=True)
    host = models.ForeignKey(
        "users.User", related_name="houses", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
