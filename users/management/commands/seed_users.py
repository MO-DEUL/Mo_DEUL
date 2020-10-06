from django.core.management.base import BaseCommand
from users import models as user_models
from django_seed import Seed
import random


class Command(BaseCommand):

    help = "This command create many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            user_models.User, number, {
                "is_superuser": False,
                "age": lambda x: random.radint(19, 80),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number} Users has been created"))
