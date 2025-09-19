from django.urls import path 
from . import views
urlpatterns = [
				path('home/',views.home,name='home'),
				path('about/',views.about,name='about'),
				path('contact/',views.contact,name='contact'),
				path('register/',views.register,name='register' ),
				path('login/',views.login,name='login'),
                path('dashboard/',views.dashboard,name='dashboard'),
                path('dashboard/courses/',views.courses,name='courses'),
                path('save_courses/', views.save_courses, name='save_courses'),
                path('dashboard/profiledit/',views.profiledit,name='profiledit'),
                path('dashboard/changepass/',views.changepass,name='changepass'),
                path('dashboard/first/',views.first,name='first'),
                path('dashboard/first/otp/',views.otp,name='otp'),
                path('dashboard/forgot/',views.forgot,name='forgot'),
                path('dashboard/forgot/otp/',views.forgot_otp,name='forgot_otp'),
                path('dashboard/logout/',views.log_out, name="log_out"),
                
                path('unique/',views.unique,name='unique'),
				]