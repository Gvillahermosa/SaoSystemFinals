from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('requestgmc', views.requestgmc, name="requestgmc"),
    path('adminmain', views.adminhome, name="adminmain"),
    path('requested-gmc', views.adminRequestedGmc, name='adminRequestedGmc'),
    path('gmc-form', views.gmcform, name="gmcform"),
    path('generate-gmc/<int:request_id>/', views.generateGmc, name='generateGmc'),
    path('monthlyCalendar', views.monthlyCalendar, name='monthlyCalendar'),
    path('monthlyCalendarAdmin', views.monthlyCalendarAdmin, name='monthlyCalendarAdmin'),
   
]