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
    path("news/",news_view),
    # path("news/<int:id>/",news_view),
    # path("holiday/",holiday_view),
    # path("holiday/<int:id>/",holiday_view),
    # path("event/",event_view),
    # path("event/<int:id>/",event_view),
    # path("visitor/",visitor_view),
    # path("visitor/<int:id>/",visitor_view),
    # path("attandance/",attandance_view),
    # path("attandance/<int:id>/",attandance_view),
    # path("payroll/",payroll_view),
    # path("payroll/<int:id>/",payroll_view),
    # path("accounting/",accounting_view),
    # path("accounting/<int:id>/",accounting_view),
    # path("designation/",designation_view),
    # path("designation/<int:id>/",designation_view),
    # path("employee/",employee_view),
    # path("employee/<int:id>/",employee_view),
    # path("teacher/",teacher_view),
    # path("teacher/<int:id>/",teacher_view),
    # path("class/",class_view),
    # path("class/<int:id>/",class_view),
    # path("section/",section_view),
    # path("subject/<int:id>/",subject_view),
    # path("rutine/",rutine_view),
    # path("rutine/<int:id>/",rutine_view),
    # path("syllabus/",syllabus_view),
    # path("syllabus/<int:id>/",syllabus_view),
    # path("student/",student_view),
    # path("student/<int:id>/",student_view),
    # path("gurdian/",gurdian_view),
    # path("gurdian/<int:id>/",gurdian_view),
    # path("student_attandance/",studentattandance_view),
    # path("student_attandance/<int:id>/",studentattandance_view),
    # path("assignment/",assignment_view),
    # path("assignment/<int:id>/",assignment_view),
    # path("exam_grade/",examgrade_view),
    # path("exam_grade/<int:id>/",examgrade_view),
    # path("examt_term/",examterm_view),
    # path("examt_term/<int:id>/",examterm_view),
    # path("exam_schedule/",examschedule_view),
    # path("exam_schedule/<int:id>/",examschedule_view),
    # path("subject/",examattandance_view),
    # path("subject/<int:id>/",examattandance_view),
    # path("book/",book_view),
    # path("book/<int:id>/",book_view),
    # path("issue/",issue_view),
    # path("issue/<int:id>/",issue_view),
    # path("fine/",fine_view),
    # path("fine/<int:id>/",fine_view),
    # path("vehicle/",vehicle_view),
    # path("vehicle/<int:id>/",vehicle_view),
    # path("route/",route_view),
    # path("route/<int:id>/",route_view),
    # path("transport_member/",transportmember_view),
    # path("transport_member/<int:id>/",transportmember_view),

]




