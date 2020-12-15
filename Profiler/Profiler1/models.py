from django.db import models


# Create your models here.


class StudentNew(models.Model):
    regNo = models.CharField(primary_key=True, max_length=25)
    fname = models.CharField(max_length=30, unique=True)
    lname = models.CharField(max_length=20)
    pword = models.CharField(default=12345, max_length=20, null=False)
    emaill = models.EmailField(max_length=30, null=False)
    level = models.IntegerField()
    faculty = models.CharField(max_length=15)
    department = models.CharField(max_length=25)

    def __str__(self):
        return str(self.regNo)


class StaffNew(models.Model):
    regNo = models.CharField(primary_key=True, max_length=25)
    fname = models.CharField(max_length=30, unique=True)
    lname = models.CharField(max_length=20)
    pword = models.CharField(default=12345, max_length=20, null=False)
    emaill = models.EmailField(max_length=30, null=False)

    def __str__(self):
        return str(self.regNo)


class RegisteredCoursesNew(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    courses = models.TextField()


class Reg100(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    courses = models.TextField()


class Reg200(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    courses = models.TextField()


class Reg300(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    courses = models.TextField()


class Reg400(models.Model):
    student = models.ForeignKey(StudentNew, on_delete=models.CASCADE)
    courses = models.TextField()


class PersonNew(models.Model):
    # regNo = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=30, unique=True)
    pword = models.CharField(max_length=20, null=False)
    emaill = models.EmailField(max_length=30, null=False)
    # lname = models.CharField(max_length=20)
    # level = models.IntegerField()
    # faculty = models.CharField(max_length=15)
    # deptment = models.CharField(max_length=25)
    status = models.BooleanField(default=False)


class Courses(models.Model):
    cName = models.CharField(primary_key=True, max_length=20)
    cUnits = models.IntegerField()
    cLevel = models.IntegerField()
    cDescrp = models.CharField(max_length=100)
