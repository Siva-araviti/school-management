import random
import django
import os
# must be on top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from faker import Faker

# must come after django setup()
from students.models import Student
from django.contrib.auth.models import User
import traceback
from rolepermissions.roles import assign_role

fakegen = Faker()



def generate_student(n=10):
    for entry in range(n):
        #user fields
        username = fakegen.name()
        first_name = username
        email = fakegen.email()
        #student fields
        registration_number = fakegen.random_int(min=10000, max=99999, step=1)
        total_amount = 100000
        paid_amount = 10000
        due_amount = total_amount - paid_amount
        date_of_birth = fakegen.date()
        mobile = fakegen.phone_number()
        try:
            user = User.objects.create_user(
                username=username, first_name=first_name, email=email, password=username
            )
            student = Student.objects.get_or_create(
                registration_number=registration_number,
                total_amount=total_amount,
                paid_amount=paid_amount,
                due_amount=due_amount,
                date_of_birth=date_of_birth,
                user=user,
                mobile=mobile)
            assign_role(user, 'student')
            print("Student user name:-", username+"  Password:- "+username)
        except Exception as e:
            print(traceback.format_exc())
        
        


if __name__ == "__main__":
    print('Creating Fake Teachers....')
    n = int(input('How many students do you wanna create?'))
    generate_student(n)
    print('students created successfully.')
