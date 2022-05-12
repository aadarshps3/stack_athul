from django.urls import path

from homeservice_app import views, adminviews, workerviews, customerviews,face_detect

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('worker_register/', views.worker_register, name='worker_register'),
    path('customer_register/', views.customer_register, name='customer_register'),

    path('admin_home/', adminviews.admin_home, name='admin_home'),
    path('workers_view/', adminviews.view_workers, name='workers_view'),
    path('workers_update/<int:id>/', adminviews.workers_update, name='workers_update'),
    path('worker_remove/<int:id>/', adminviews.remove_worker, name='worker_remove'),
    path('customers_view/', adminviews.view_customers, name='customers_view'),
    path('customers_remove/<int:id>/', adminviews.remove_customers, name='customers_remove'),
    path('work_add/', adminviews.add_work, name='work_add'),
    path('work_view/', adminviews.view_work, name='work_view'),
    path('work_update/<int:id>/', adminviews.update_work, name='work_update'),
    path('work_delete/<int:id>/', adminviews.delete_work, name='work_delete'),
    path('appointment_admin', adminviews.appointment_admin, name='appointment_admin'),
    path('approve_appointment/<int:id>/', adminviews.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', adminviews.reject_appointment, name='reject_appointment'),
    path('Feedback_admin/', adminviews.Feedback_admin, name='Feedback_admin'),
    path('reply_Feedback/<int:id>/', adminviews.reply_Feedback, name='reply_Feedback'),
    path('add_bill/', adminviews.bill, name='add_bill'),
    path('view_bill/', adminviews.view_bill, name='view_bill'),

    path('worker_home/', workerviews.worker_home, name='worker_home'),
    path('schedule_add/', workerviews.schedule_add, name='schedule_add'),
    path('schedule_views', workerviews.schedule_view, name='schedule_views'),
    path('schedule_update/<int:id>/', workerviews.schedule_update, name='schedule_update'),
    path('schedule_delete/<int:id>/', workerviews.schedule_delete, name='schedule_delete'),
    path('view_bill_worker/', workerviews.view_bill_worker, name='view_bill_worker'),
    path('appointment_view_worker/', workerviews.appointment_view_worker, name='appointment_view_worker'),

    path('customer_home/', customerviews.customer_home, name='customer_home'),
    path('view_workers/', customerviews.view_workers_customer, name='view_workers'),
    path('view_schedule/', customerviews.view_schedule_customer, name='view_schedule'),
    path('take_appointment/<int:id>/', customerviews.take_appointment, name='take_appointment'),
    path('appointment_view', customerviews.appointment_view, name='appointment_view'),
    path('Feedback_add_user', customerviews.Feedback_add_user, name='Feedback_add_user'),
    path('Feedback_view_user', customerviews.Feedback_view_user, name='Feedback_view_user'),
    path('view_bill_user', customerviews.view_bill_user, name='view_bill_user'),
    path('pay_bill/<int:id>/', customerviews.pay_bill, name='pay_bill'),
    path('face', face_detect.face, name='face'),
    path('pay_in_direct/<int:id>/', customerviews.pay_in_direct, name='pay_in_direct'),
    path('bill_history', customerviews.bill_history, name='bill_history'),
    # path('successfull',customerviews.successful, name='succesfull'),

]
