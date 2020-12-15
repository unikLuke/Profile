# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .forms import RegForm
from .functions import my_function, my_function2
from .models import StudentNew, StaffNew, PersonNew, Courses, Reg400, Reg300, Reg200, Reg100


@require_http_methods(['GET', 'POST'])
def home_view(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            PersonNew.objects.create(name=form.cleaned_data.get('name'),
                                     pword=form.cleaned_data.get('password'),
                                     emaill=form.cleaned_data.get('email'),
                                     status='True')
            messages.success(request, 'Register Success!')
        return redirect('login_view')
    else:
        form = RegForm()
        return render(request, 'profileLoger/home.html', {})


@require_http_methods(['GET', 'POST'])
def login_view(request):
    text = '''Login Form'''
    return render(request, 'Profiler1/login.html', {'text': text, })


@require_http_methods(['POST', ])
def tesst(request, ):
    if request.method == 'POST':
        Students = StudentNew.objects.all()
        Staffs = StaffNew.objects.all()
        if len(Students) | len(Staffs) > 0:
            regNo = request.POST.get('RegNo')
            pword = request.POST.get('password')
            for student in Students:
                if (str(student.regNo) == regNo) & (student.pword == pword):
                    return render(request, 'Profiler1/index.html', {'student': student})
            for staff in Staffs:
                if (str(staff.regNo) == regNo) & (staff.pword == pword):
                    return render(request, 'Profiler1/indexStaff.html', {'staff': staff})
            for student in Students:
                if str(student.regNo) == regNo:
                    return HttpResponse('Error: RegNo or Passowrd Student databese')
            for staff in Staffs:
                if str(staff.regNo) == regNo:
                    return HttpResponse('Error: RegNo or Passowrd Staff database')
            return HttpResponse("No Record in the database Second to Last level")
        else:
            return HttpResponse("No Record in the database Last level here..")


@require_http_methods(['POST', ])
def tes(request, student_di):
    if request.method == 'POST':
        if StudentNew.objects.get(regNo=str(student_di)):
            student = StudentNew.objects.get(regNo=str(student_di))
            text = 'First Name : ' + student.fname + '<br>'
            text += 'Last Name : ' + student.lname + '<br>'
            text += 'Department : ' + student.department + '<br>'
            if request.POST.get("register"):

                what = int(student.level) + 1
                return render(request, 'Profiler1/to_regCourses.html',
                              {'who': student_di, 'student': student, 'range': range(100, what, 100)})

            elif request.POST.get('registered'):
                what = int(student.level) + 1
                return render(request, 'Profiler1/regCourses.html',
                              {'who': student_di, 'student': student, 'range': range(100, what, 100)})

            elif request.POST.get('profile'):
                text += 'Button Clicked is Profile..'

            return HttpResponse(text)
        else:
            return HttpResponse("No record of you found contact Admin")
    else:
        return HttpResponse("Hello World this is here...")


@require_http_methods(['POST', ])
def tes2(request, staff_di):
    if request.method == 'POST':
        if StaffNew.objects.get(regNo=str(staff_di)):
            staff = StaffNew.objects.get(regNo=str(staff_di))
            text = 'First Name : ' + staff.fname + '<br>'
            text += 'Last Name : ' + staff.lname + '<br>'
            if request.POST.get("fresh"):
                text += 'Student Offering Course for the First time'

            elif request.POST.get('cov'):
                text += 'Student as Carry Overs'

            elif request.POST.get('profile'):
                text += 'Button Clicked is Profile..'

            return HttpResponse(text)

        else:
            return HttpResponse("No record of you found contact Admin")
    else:
        return HttpResponse("Hello World this is here...")


@require_http_methods(['POST', ])
def to_regCourses(request, student_di):
    if request.method == 'POST':
        # student = get_object_or_404(StudentNew, pk=student_di)
        level = int(request.POST.get('level'))
        if level == 100:
            courses = Courses.objects.filter(cLevel=100).order_by('cLevel')
            you = student_di
            level = 100
            return render(request, 'Profiler1/table.html', {'courses': courses, 'person': you, 'level': level})
        elif level == 200:
            courses = Courses.objects.filter(cLevel__lte=200).order_by('cLevel')
            you = student_di
            level = 200
            return render(request, 'Profiler1/table.html', {'courses': courses, 'person': you, 'level': level})
        elif level == 300:
            courses = Courses.objects.filter(cLevel__lte=300).order_by('cLevel')
            you = student_di
            level = 300
            return render(request, 'Profiler1/table.html', {'courses': courses, 'person': you, 'level': level})
        elif level == 400:
            level = 400
            courses = Courses.objects.filter(cLevel__lte=400).order_by('cLevel')
            you = student_di
            return render(request, 'Profiler1/table.html', {'courses': courses, 'person': you, 'level': level})
        else:
            return HttpResponse("Oops!! No course actually available for this level; please contact the admin")


@require_http_methods(['POST', ])
def regCourses(request, student_di):
    global course
    if request.method == 'POST':
        level = int(request.POST.get('level'))
        student = get_object_or_404(StudentNew, pk=student_di)
        if level == 100:
            courses = Reg100.objects.all().filter(student__regNo=student_di)
            if len(courses) > 0:
                lis = courses[0].courses
                course = [s.split('-') for s in lis.split(',')]
                return render(request, 'Profiler1/readyCourses.html',
                              {'student': student, 'Level': level, 'courses': course})
            else:
                return HttpResponse("there is No Record of the Registered Courses for the Level Contact admin"
                                    + str(student_di))
        elif level == 200:
            courses = Reg200.objects.all().filter(student__regNo=student_di)
            if len(courses) > 0:
                lis = courses[0].courses
                course = [s.split('-') for s in lis.split(',')]
                return render(request, 'Profiler1/readyCourses.html',
                              {'student': student, 'Level': level, 'courses': course})
            else:
                return HttpResponse("there is No Record of the Registered Courses for the Level Contact admin"
                                    + str(student_di))
        elif level == 300:
            courses = Reg300.objects.filter(student__regNo=student_di)
            if courses:
                if len(courses) > 1:
                    return HttpResponse(" This is just testing something " + len(courses))
            else:
                return HttpResponse("there is No Record of the Registered Courses for the Level Contact admin"
                                    + str(student_di))

        elif level == 400:
            courses = Reg400.objects.filter(student_regNo=student_di)
            if courses:
                if len(courses) > 1:
                    return HttpResponse(" This is just testing something " + len(courses))
            else:
                return HttpResponse("there is No Record of the Registered Courses for the Level Contact admin"
                                    + str(student_di))

        else:
            return HttpResponse("Oops!! No course actually available for this level; please contact the admin")


@require_http_methods(['POST', ])
def regcourseview(request, person, level):
    mychoice_course1 = ""
    student = get_object_or_404(StudentNew, pk=person)
    level1 = int(level)
    if request.method == 'POST':
        courses = Courses.objects.filter(cLevel__lte=level)
        if level1 == 100:
            registered_courses = Reg100.objects.all()
        elif level1 == 200:
            registered_courses = Reg200.objects.all()
        elif level1 == 300:
            registered_courses = Reg300.objects.all()
        elif level1 == 400:
            registered_courses = Reg400.objects.all()
        else:
            return HttpResponse("Nothing to show here for now, wait for the admin")
        for course in courses:
            testa = request.POST.get(course.cName, 'False')
            if testa != 'False':
                mychoice_course1 += course.cName + '-' + str(course.cUnits) + '-' + str(
                    course.cLevel) + '-' + course.cDescrp + ','
        if len(registered_courses) > 0:
            if len(mychoice_course1) > 1:
                for cor in registered_courses:
                    if cor.student.regNo == person:
                        cor.courses = mychoice_course1
                        cor.save()
                        return HttpResponse("Courses Registered Updated Successful")
                if my_function(level1, mychoice_course1, student):
                    return HttpResponse("Courses Registered First time in already populated table Successful")
        elif len(mychoice_course1) > 1:
            if my_function2(level1, mychoice_course1, student):
                return HttpResponse("Courses Registered Successful First time Only")
        else:
            return HttpResponse('No Course selected...')
