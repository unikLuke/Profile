from .models import Reg400, Reg300, Reg200, Reg100


# ('Reg' + level).objects.create(courses=mychoice_course1, student=student)
def my_function(level, courses, student):
    if level == 100:
        Reg100.objects.create(courses=courses, student=student)
    elif level == 200:
        Reg200.objects.create(courses=courses, student=student)
    elif level == 300:
        Reg300.objects.create(courses=courses, student=student)
    else:
        Reg400.objects.create(courses=courses, student=student)
    return 'True'


def my_function2(level, courses, student):
    if level == 100:
        Reg100.objects.create(courses=courses, student=student)
    elif level == 200:
        Reg200.objects.create(courses=courses, student=student)
    elif level == 300:
        Reg300.objects.create(courses=courses, student=student)
    else:
        Reg400.objects.create(courses=courses, student=student)
    return 'True'
