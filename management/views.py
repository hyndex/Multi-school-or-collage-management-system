from management.models import *
from management.serializers import *
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class NoticeView(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class NoticeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = NoticeSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class NewsView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class HolidayView(generics.ListCreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class HolidayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VisitorView(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class VisitorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AttandanceView(generics.ListCreateAPIView):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class AttandanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PayrollView(generics.ListCreateAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class PayrollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AccountingView(generics.ListCreateAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class AccountingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DesignationView(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class DesignationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ClassView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SectionView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RutineView(generics.ListCreateAPIView):
    queryset = Rutine.objects.all()
    serializer_class = RutineSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class RutineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rutine.objects.all()
    serializer_class = RutineSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ExamAttandanceView(generics.ListCreateAPIView):
    queryset = ExamAttandance.objects.all()
    serializer_class = ExamAttandanceSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ExamAttandanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamAttandance.objects.all()
    serializer_class = ExamAttandanceSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SyllabusView(generics.ListCreateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class SyllabusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class GurdianView(generics.ListCreateAPIView):
    queryset = Gurdian.objects.all()
    serializer_class = GurdianSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class GurdianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gurdian.objects.all()
    serializer_class = GurdianSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentAttandanceView(generics.ListCreateAPIView):
    queryset = StudentAttandance.objects.all()
    serializer_class = StudentAttandanceSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class StudentAttandanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAttandance.objects.all()
    serializer_class = StudentAttandanceSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AssignmentView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ExamGradeView(generics.ListCreateAPIView):
    queryset = ExamGrade.objects.all()
    serializer_class = ExamGradeSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ExamGradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamGrade.objects.all()
    serializer_class = ExamGradeSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ExamTermView(generics.ListCreateAPIView):
    queryset = ExamTerm.objects.all()
    serializer_class = ExamTermSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ExamTermDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamTerm.objects.all()
    serializer_class = ExamTermSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ExamScheduleView(generics.ListCreateAPIView):
    queryset = ExamSchedule.objects.all()
    serializer_class = ExamScheduleSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ExamScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamSchedule.objects.all()
    serializer_class = ExamScheduleSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class IssueView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class IssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FineView(generics.ListCreateAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class FineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RouteView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class RouteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TransportMemberView(generics.ListCreateAPIView):
    queryset = TransportMember.objects.all()
    serializer_class = TransportMemberSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class TransportMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransportMember.objects.all()
    serializer_class = TransportMemberSerializer
    lookup_field='id'
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
