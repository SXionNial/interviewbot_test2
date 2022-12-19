from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        User.objects.create_superuser(
            email='adminrawr@gmail.com',
            password='Pass123.',
            firstname = 'Angelll',
            lastname = 'Singsonss',
            gender = 'Male',
            phone = '09054592625',
        )
        