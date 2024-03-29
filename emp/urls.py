from django.contrib import admin
from django.urls import path,include
from emp import views

urlpatterns = [
    path('home/',views.home),
    path('add-emp/',views.add_emp),
    path('delete-emp/<int:emp_id>',views.delete_emp),
    path('update-emp/<int:emp_id>',views.update_emp),
    path('do-update-emp/<int:emp_id',views.do_update_emp),
]