from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('tasks_and_assignments', views.tasks_and_assignments, name='tasks_and_assignments'),
    path('assign_task/<str:application_number>', views.assign_task, name='assign_task'),
    path('assign_task_marriage/<str:pk>', views.assign_task_marriage, name='assign_task_marriage'),
    path('assigned_to_me', views.assigned_to_me, name='assigned_to_me'),
    path('add_officer_note/<str:application_number>', views.add_officer_note, name='add_officer_note'),
    path('add_officer_note_marriage/<str:pk>', views.add_officer_note_marriage, name='add_officer_note_marriage'),

    # OLD BUT FUNCTIONAL
    path('role', views.role, name='role'),
    path('add_role', views.add_role, name='add_role'),
    path('update_role/<int:pk>', views.update_role, name='update_role'),
    path('delete_role/<int:pk>', views.delete_role, name='delete_role'),

    path('account', views.account, name='account'),

]
