from django.contrib import admin
from django.urls import path
from django.urls import include, path
from management.views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("news",NewsViewSet)
# router.register("holiday",HolidayViewSet)
# router.register("event",EventViewSet)
# router.register("visitor",VisitorViewSet)
# router.register("attandance",AttandanceViewSet)
# router.register("payroll",PayrollViewSet)
# router.register("accounting",AccountingViewSet)
# router.register("designation",DesignationViewSet)
# router.register("employee",EmployeeViewSet)
# router.register("teacher",TeacherViewSet)
# router.register("class",ClassViewSet)
# router.register("section",SectionViewSet)
# router.register("subject",SubjectViewSet)
# router.register("rutine",RutineViewSet)
# router.register("syllabus",SyllabusViewSet)
# router.register("student",StudentViewSet)
# router.register("gurdian",GurdianViewSet)
# router.register("studentattandance",StudentAttandanceViewSet)
# router.register("assignment",AssignmentViewSet)
# router.register("examgrade",ExamGradeViewSet)
# router.register("examTterm",ExamTermViewSet)
# router.register("examschedule",ExamScheduleViewSet)
# router.register("subject",ExamAttandanceViewSet)
# router.register("book",BookViewSet)
# router.register("issue",IssueViewSet)
# router.register("fine",FineViewSet)
# router.register("vehicle",VehicleViewSet)
# router.register("route",RouteViewSet)
# router.register("transportmember",TransportMemberViewSet)

urlpatterns = [
    path("api/news/",NewsView.as_view()),
    path("api/news/",NewsDetailView.as_view()),
    path("api/holiday/",HolidayView.as_view()),
    path("api/holiday/",HolidayDetailView.as_view()),
    path("api/event/",EventView.as_view()),
    path("api/event/",EventDetailView.as_view()),
    path("api/visitor/",VisitorView.as_view()),
    path("api/visitor/",VisitorDetailView.as_view()),
    path("api/attandance/",AttandanceDetailView.as_view()),
    path("api/attandance/",AttandanceView.as_view()),
    path("api/payroll/",PayrollView.as_view()),
    path("api/payroll/",PayrollDetailView.as_view()),
    path("api/accounting/",AccountingView.as_view()),
    path("api/accounting/",AccountingDetailView.as_view()),
    path("api/designation/",DesignationDetailView.as_view()),
    path("api/designation/",DesignationView.as_view()),
    path("api/designation/",DesignationDetailView.as_view()),
    path("api/employee/",EmployeeView.as_view()),
    path("api/employee/",EmployeeDetailView.as_view()),
    path("api/teacher/",TeacherView.as_view()),
    path("api/teacher/",TeacherDetailView.as_view()),
    path("api/class/",ClassView.as_view()),
    path("api/class/",ClassDetailView.as_view()),
    path("api/section/",SectionView.as_view()),
    path("api/section/",SectionDetailView.as_view()),
    path("api/subject/",SubjectView.as_view()),
    path("api/subject/",SubjectDetailView.as_view()),
    path("api/rutine/",RutineView.as_view()),
    path("api/rutine/",RutineDetailView.as_view()),
    path("api/syllabus/",SyllabusView.as_view()),
    path("api/syllabus/",SyllabusDetailView.as_view()),
    path("api/student/",StudentView.as_view()),
    path("api/student/",StudentDetailView.as_view()),
    path("api/gurdian/",GurdianView.as_view()),
    path("api/gurdian/",GurdianDetailView.as_view()),
    path("api/studentattandance/",StudentAttandanceView.as_view()),
    path("api/studentattandance/",StudentAttandanceDetailView.as_view()),
    path("api/assignment/",AssignmentView.as_view()),
    path("api/assignment/",AssignmentDetailView.as_view()),
    path("api/examgrade/",ExamGradeView.as_view()),
    path("api/examgrade/",ExamGradeDetailView.as_view()),
    path("api/examTterm/",ExamTermView.as_view()),
    path("api/examTterm/",ExamTermDetailView.as_view()),
    path("api/examschedule/",ExamScheduleView.as_view()),
    path("api/examschedule/",ExamScheduleDetailView.as_view()),
    path("api/subject/",ExamAttandanceView.as_view()),
    path("api/subject/",ExamAttandanceDetailView.as_view()),
    path("api/book/",BookView.as_view()),
    path("api/book/",BookDetailView.as_view()),
    path("api/issue/",IssueView.as_view()),
    path("api/issue/",IssueDetailView.as_view()),
    path("api/fine/",FineView.as_view()),
    path("api/fine/",FineDetailView.as_view()),
    path("api/vehicle/",VehicleView.as_view()),
    path("api/vehicle/",VehicleDetailView.as_view()),
    path("api/route/",RouteView.as_view()),
    path("api/route/",RouteDetailView.as_view()),
    path("api/transportmember/",TransportMemberView.as_view()),
    path("api/transportmember/",TransportMemberDetailView.as_view()),

]




