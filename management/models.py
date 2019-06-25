from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from users.models import School, Chain, Profile, Owner

#################################################################################################
#  Common to all modules
#################################################################################################

class Notice(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Notice_owner')
    title = models.CharField(max_length=150, blank=True, null=True, default='')
    notice = models.TextField(max_length=1000, blank=True, null=True, default='')
    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    on_web = models.BooleanField(default=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

class News(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='News_owner')
    title = models.CharField(max_length=150, blank=True, null=True, default='')
    news = models.TextField(max_length=1000, blank=True, null=True, default='')
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    on_web = models.BooleanField(default=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

class Holiday(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Holiday_owner')
    title = models.CharField(max_length=150, blank=True, null=True, default='')
    expiry_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    on_web = models.BooleanField(default=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

class Event(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Event_owner')
    title = models.CharField(max_length=150, blank=True, null=True, default='')
    event = models.CharField(max_length=1000, blank=True, null=True, default='')
    place = models.CharField(max_length=150, blank=True, null=True, default='')
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    on_web = models.BooleanField(default=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

class Visitor(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Visitor_owner')
    Name = models.CharField(max_length=150, blank=True, null=True, default='')
    user_to_meet = models.CharField(max_length=150, blank=True, null=True, default='')
    reason = models.CharField(max_length=150, blank=True, null=True, default='')
    address = models.CharField(max_length=150, blank=True, null=True, default='')
    phone = models.CharField(max_length=20, blank=True, null=True, default='')
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

class Attandance(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Attandance_owner')
    user =  models.CharField(max_length=30, blank=False, null=False)
    attandance = models.CharField(max_length=10, blank=True, null=True, default='')
    date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

class Payroll(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Payroll_owner')
    name = models.CharField(max_length=20, blank=True, null=True, default='')
    salary = models.FloatField()
    allowance = models.FloatField()
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Accounting(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Accounting_owner')
    created_by = models.CharField(max_length=30, blank=True, null=True)
    paid_to = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True, default='')
    Amount = models.FloatField()
    is_income = models.BooleanField(default=False)
    payment_category = models.CharField(max_length=20, blank=True, null=True, default='')
    paid_status = models.BooleanField(default=True)
    date = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=20, blank=True, null=True, default='')


class Designation(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Designation_owner')
    designation = models.CharField(max_length=10, blank=True, null=True, default='')
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Employee(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Employee_owner')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    salary_grade = models.ForeignKey(Payroll, on_delete=models.PROTECT, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    Qualification = models.CharField(max_length=30, blank=True, null=True, default='')
    resume = models.FileField(upload_to='media/resume/',blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)

#################################################################################################
#  School Specific Modules
#################################################################################################

class Teacher(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Teacher_owner')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Class(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Class_owner')
    name = models.CharField(max_length=30, blank=True, null=True, default='')
    numaric_name = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, default='')
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Section(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Section_owner')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True, default='')
    teacher = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Subject(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Subject_owner')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30, blank=True, null=True, default='')
    subject_code = models.CharField(max_length=10, blank=True, null=True, default='')
    book = models.CharField(max_length=30, blank=True, null=True, default='')
    is_compalsory = models.BooleanField(default=True)
    teacher = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.PROTECT,  blank=True, null=True)

class Rutine(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Rutine_owner')
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField()    
    end_time = models.DateTimeField()    
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Syllabus(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Syllabus_owner')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    syllabus = models.FileField(upload_to='media/syllabus/',blank=True, null=True)    
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Student(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Student_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.PROTECT, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, blank=True, null=True)
    privious_school = models.CharField(max_length=50, blank=False, null=False)
    privious_class = models.CharField(max_length=20, blank=False, null=False)
    tc = models.FileField(upload_to='media/tc/',blank=True, null=True)    
    created_by = models.CharField(max_length=30, blank=True, null=True)


class Gurdian(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Gurdian_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class StudentAttandance(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='StudentAttandance_owner')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    attandance = models.CharField(max_length=10, blank=False, null=False)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Assignment(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Assignment_owner')
    title = models.CharField(max_length=30, blank=False, null=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    deadline = models.DateField()
    assignment = models.FileField(upload_to='media/assignment/',blank=True, null=True) 
    created_by = models.CharField(max_length=30, blank=True, null=True)


class ExamGrade(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='ExamGrade_owner')
    grade = models.CharField(max_length=30, blank=False, null=False)
    point = models.IntegerField(blank=True, null=True)
    marks_from = models.IntegerField(blank=False, null=False)
    marks_to = models.IntegerField(blank=False, null=False)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class ExamTerm(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='ExamTerm_owner')
    name = models.CharField(max_length=30, blank=False, null=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class ExamSchedule(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='ExamSchedule_owner')
    exam_term = models.ForeignKey(ExamTerm, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateField()
    created_by = models.CharField(max_length=30, blank=True, null=True)

class ExamAttandance(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='ExamAttandance_owner')
    exam_schedule = models.ForeignKey(ExamSchedule, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attandance = models.CharField(max_length=10, blank=False, null=False, default='Present')
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Book(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Book_owner')
    name = models.CharField(max_length=30, blank=False, null=False)
    author = models.CharField(max_length=30, blank=False, null=False)
    condition = models.CharField(max_length=30, blank=False, null=False)
    language = models.CharField(max_length=30, blank=False, null=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Issue(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Issue_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(User,  on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    remark = models.CharField(max_length=150, blank=False, null=False)
    created_by = models.CharField(max_length=30, blank=True, null=True)


class Fine(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Fine_owner')
    extra_day = models.IntegerField(default=0)
    fine = models.FloatField(default=0)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Vehicle(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Vehicle_owner')
    number_palte = models.CharField(max_length=30, blank=True, null=True)
    registration_number = models.CharField(max_length=30, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    driver = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Route(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Route_owner')
    title = models.CharField(max_length=30, blank=True, null=True)
    stop_name = models.CharField(max_length=30, blank=True, null=True)
    stop_fare = models.FloatField(default=0)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class TransportMember(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='TransportMember_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)

class Hostel(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Hostel_owner')
    name = models.CharField(max_length=30, blank=False, null=False)
    type = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)


class Room(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='Room_owner')
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT, blank=True, null=True)
    room = models.CharField(max_length=30, blank=False, null=False)
    seat = models.IntegerField(default=0)
    cost = models.FloatField(default=0)
    created_by = models.CharField(max_length=30, blank=True, null=True)


class HostelMember(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,  related_name='HostelMember_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30, blank=True, null=True)
