from django.contrib.auth.models import User, Group
from rest_framework import serializers
from management.models import *

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields='__all__'

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields='__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields='__all__'

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields='__all__'

class AttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attandance
        fields='__all__'

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields='__all__'

class AccountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounting
        fields='__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields='__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields='__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields='__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields='__all__'

class RutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutine
        fields='__all__'

class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'

class GurdianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gurdian
        fields='__all__'

class StudentAttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttandance
        fields='__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields='__all__'

class ExamGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamGrade
        fields='__all__'

class ExamTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTerm
        fields='__all__'

class ExamScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSchedule
        fields='__all__'

class ExamAttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields='__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields='__all__'

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields='__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields='__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields='__all__'

class TransportMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMember
        fields='__all__'