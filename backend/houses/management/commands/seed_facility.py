from django.core.management.base import BaseCommand
from houses import models as house_models


class Command(BaseCommand):
    help = 'This command create facilities for houses.'

    def handle(self, *args, **options):
        facilities = [
            "건물 내 무료 주차",
            "헬스장",
            "자쿠지",
            "수영장",
        ]
        for f in facilities:
            house_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))
