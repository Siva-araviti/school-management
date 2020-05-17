from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'create_stuff': True,
        'create_teacher': True,
        'admin':True
    }

class Student(AbstractUserRole):
    available_permissions = {
        'create_stuff': True,
        'create_teacher': True,
        'student_obj':True
    }

class Teacher(AbstractUserRole):
    available_permissions = {
        'create_stuff': True,
        'create_teacher': True,
        'teacher':True
    }
class Stuff(AbstractUserRole):
    available_permissions = {
        'create_teacher': True,
        'stuff':True
    }
