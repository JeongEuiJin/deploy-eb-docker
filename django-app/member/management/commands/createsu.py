import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    def handel(self,*args,**options):
        config_secret_common = json.loads(settings.CONFIG_SECRET_COMMON_FILE).read()
        username = config_secret_common['django']['default_superuser']['username']
        password = config_secret_common['django']['default_superuser']['password']
        if not User.objcets.filter(username=username).exist():
            User.objcets.create_superuser(
                username=username,
                password=password,
                email=''
            )
            print('Superuser %s created' % username)
        else:
            print('Superuser %s is already exist' % username)