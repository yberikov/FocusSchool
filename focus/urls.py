from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('focusplan1/', views.focusplan1, name='focusplan1'),
    path('teacher_evaluation/', views.teacher_evaluation, name='teacher_evaluation'),
    path('observer_evaluation/', views.observer_evaluation, name='observer_evaluation'),
    path('report_details/<int:id>/', views.report_details, name='report_details'),
    path('focusteach1/', views.focusteach1, name='focusteach1'),
    path('focusevaluation1', views.focusevaluation1, name='focusevaluation1'),
    path('focuscomplex1', views.focuscomplex1, name='focuscomplex1'),
    path('admin_panel', views.admin_panel, name='admin_panel'),

]