from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin').exists():
            User.objects.create_superuser(
                email='admin',
                password='pass123',
                firstname = 'Angel',
                lastname = 'Singson',
                gender = 'Male',
                phone = '09054592625',
            )
        print('Superuser has been created.')