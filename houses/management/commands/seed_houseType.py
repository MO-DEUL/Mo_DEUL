from django.core.management import BaseCommand
from django_seed import Seed
from houses import models as house_models


class Command(BaseCommand):

    help = "Add house types to DB"

    def handle(self, *args, **options):
        house_types = [
            "주택",
            "아파트",
            "B&B",
            "부티크 호텔",
            "게스트 스위트",
            "게스트용 별채",
            "레지던스",
            "로프트",
            "리조트",
            "방갈로",
            "저택",
            "전원주택",
        ]

        for h in house_types:
            house_models.HouseType.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS("House Types has been created!"))
