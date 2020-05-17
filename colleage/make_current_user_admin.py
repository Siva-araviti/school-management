import django
import os
from django.http import HttpRequest as request
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
# must come after django.setup()
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role

user  = User.objects.get(is_superuser=1)
assign_role(user, 'admin')