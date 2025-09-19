from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from .forms import *
from .models import *
from myapp.models import Studentsdbase
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    user_email = request.session.get('logged_user')
    return render(request,'home.html')
def unique(request):
    user_email = request.session.get('logged_user')
    return render(request,'photo.html')
def about(request):
    user_email = request.session.get('logged_user')
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
            name=request.POST['name']
            From_email=request.POST['email']
            tomail = "muhammedalinoushad7@gmail.com"
            subject=request.POST['subject']
            message=request.POST['message']
            phone_no=request.POST['phone_no']
            letter=f"""
Hello Scope India Team...
My Contact details -
                            
Name:  {name}      
Email: {From_email}
Phone: {phone_no}
Message: {message}

Thank you for Contact us !
"""
            mail=EmailMessage(subject,letter,From_email,[tomail])
            print(mail)
            mail.send()    
    return render(request,'contact.html')

def register(request):
    if request.method=="POST":
        
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')      
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        hobbies=request.POST.getlist('hobbies')
        file=request.FILES.get('file')
        
        studentobj=Studentsdbase()
        print(Studentsdbase)
        studentobj.fname_db=fname
        studentobj.lname_db=lname
        studentobj.dob_db=dob
        studentobj.email_db=email
        studentobj.phone_db=phone
        studentobj.gender_db=gender
        studentobj.country_db=country
        studentobj.state_db=state
        studentobj.city_db=city
        studentobj.hobbies_db=hobbies
        studentobj.file_db=file
        studentobj.save() 

        subject = "New Registration Confirmation"
        message = f"""
Hello Scope India Team,

My Name is {fname} {lname}.
Your registration details:
First Name: {fname}
Last Name: {lname}
Date of Birth: {dob}
Email: {email}
Phone: {phone}
Gender: {gender}
Country: {country}
State: {state}
City: {city}
Hobbies: {hobbies}

Thank you for registering!
"""
        to_email = "muhammedalinoushad7@gmail.com"
        register_mail=EmailMessage(subject,message,email,[to_email])
        print(register_mail)
        register_mail.send()
        return redirect('register')

    return render(request,'register.html')

def first(request):
    if request.method=="POST":
        otp_send=str(random.randint(10000,99999))
        get_emails=request.POST.get('email')
        try:
            user_email =Studentsdbase.objects.get(email_db=get_emails)
            user_email.otp_db = otp_send
            user_email.save()

            subject = "Your OTP Code for Verification"
            message = f"""
            Hello, 
            Your OTP Code is {otp_send}.
            Please enter this on the verification page.
            Regards, 
            SCOPE INDIA
            """

            send_email = EmailMessage(subject, message, "muhammedalinoushad7@gmail.com", [get_emails])
            try:
                send_email.send()
                request.session['otp'] = otp_send 
                request.session['user_email'] = get_emails  

                return redirect('otp')
            except Exception as e:
                messages.error(request, "There was an error sending the OTP email. Please try again later.")
                return redirect('first')

        except Studentsdbase.DoesNotExist:
            messages.error(request, "This email is not registered.")
            return render(request, 'first.html')
    return render(request,'first.html') 


def otp(request):
    if request.method == 'POST':
        get_otp = request.POST.get('OTP')
        get_password = request.POST.get('SetsPassword')
        user_pass = Studentsdbase.objects.get(otp_db=get_otp)
        if user_pass:
            user_pass.password_db = get_password
            user_pass.save()
            messages.success(request, "Password set successfully. Please login.")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('otp') 

    return render(request, 'otp.html')

def forgot(request):
    if request.method=="POST":
        for_otp=str(random.randint(10000,99999))
        for_mail=request.POST.get('emails')
        user_mail=Studentsdbase.objects.get(email_db=for_mail)
        if user_mail:
            user_mail.otp_db=for_otp
            user_mail.save()
        subject="Your OTP Code for varify code in Confirm new Password."
        message=f"""
============================================
Hello,
            Your OTP Code for new password is {for_otp}.
Please enter this on the verification site OTP page.
                                                    Be Regard,
                                                    SCOPE INDIA. 

============================================                                                                                                               
"""
        from_email="muhammedalinoushad7@gmail.com"
        send_email=EmailMessage(subject,message,from_email,[for_mail])
        send_email.send()
        return redirect('forgot_otp') 
    return render(request,'forgot.html')

def forgot_otp(request):
    if request.method == 'POST':
        get_otps=request.POST.get('otps')
        passwordsets=request.POST.get('passwordset')
        user_pass=Studentsdbase.objects.get(otp_db=get_otps)
        if user_pass:
            user_pass.password_db=passwordsets
            user_pass.save()
            return redirect('login')
    return render(request,'forgot_otp.html')

def login(request):
    error_messages = {}
    if request.method == "POST":
        get_mail = request.POST.get('email_login')
        get_pass = request.POST.get('pass_login')
        remember_me = request.POST.get('remember') == 'on'

        try:
            user = Studentsdbase.objects.get(email_db=get_mail)
            if get_pass == user.password_db:  
                request.session['logged_user'] = user.email_db  
                request.session['first_name'] = user.fname_db  
                request.session['last_name'] = user.lname_db  
                request.session['profile_picture'] = user.file_db.url if user.file_db else 'img/profile-placeholder.png'  
                request.session['phone'] = user.phone_db
                request.session['city'] = user.city_db
                request.session['country'] = user.country_db
                request.session['state'] = user.state_db
                request.session['hobbies'] = user.hobbies_db
                request.session['courses'] = user.courses_db
                response = redirect('dashboard')  
                if remember_me:
                    response.set_cookie('logged_user', user.email_db, max_age=1200)
                else:
                    response.delete_cookie('logged_user')
                return response
            else:
                error_messages['pass_error'] = 'Wrong password, Authentication failed!'
        except Studentsdbase.DoesNotExist:
            error_messages['email_error'] = 'User does not exist!'
    
    return render(request, "login.html", {'errors': error_messages})

def dashboard(request):
    user_email = request.session.get('logged_user')
    if not user_email:
        return redirect('login') 
    try:
        user = Studentsdbase.objects.get(email_db=user_email)
    except Studentsdbase.DoesNotExist:
        return redirect('login')

    context = {
        'user_email': user_email,
        'user_first_name': request.session.get('first_name', 'User'),
        'user_last_name': request.session.get('last_name', ''),
        'user_img': request.session.get('profile_picture', 'img/profile-placeholder.png'),
        'user_phone':request.session.get('phone'),
        'user_country':request.session.get('country'),
        'user_city':request.session.get('city'),
        'user_courser': user.courses_db.split(",") if user.courses_db else [],
        'user_hobbies':request.session.get('hobbies'),
        'user_state':request.session.get('state'),
    }
    
    return render(request, 'dashboard.html',{"context": context})

def courses(request):
    user_email = request.session.get('logged_user')
    if not user_email:
        return redirect('login')
    try:
        user = Studentsdbase.objects.get(email_db=user_email)
    except Studentsdbase.DoesNotExist:
        return redirect('login')

    context = {
        'user_email': user_email,
        'user_first_name': request.session.get('first_name', 'User'),
        'user_last_name': request.session.get('last_name', ''),
        'user_img': request.session.get('profile_picture', 'img/profile-placeholder.png')
    }

    return render(request, 'courses.html', context)

def save_courses(request):
    user_email = request.session.get('logged_user')
    if not user_email:
        return redirect('login')
    try:
        user = Studentsdbase.objects.get(email_db=user_email)
    except Studentsdbase.DoesNotExist:
        return redirect('login')

    courses = request.POST.get('courses_db', '') 
    if user.courses_db and user.courses_db == courses:
        messages.info(request, "You have already saved these courses.")
        return redirect('courses') 

    user.courses_db = courses
    user.save()

    messages.success(request, "Your courses have been successfully saved.")
    return redirect('courses')

def profiledit(request):
    user_email = request.session.get('logged_user')
    if not user_email:
        return redirect('login')
    try:
        user = Studentsdbase.objects.get(email_db = user_email)  
    except Studentsdbase.DoesNotExist:
        return redirect('login')  

    if request.method == "POST":
        if request.method == "POST":
            print(request.POST)
        if "update" in request.POST:
            user.fname_db = request.POST.get("first_name", user.fname_db)
            user.lname_db = request.POST.get("last_name", user.lname_db)
            user.gender_db = request.POST.get("gender", user.gender_db)
            user.dob_db = request.POST.get("dob", user.dob_db) 
            user.phone_db = request.POST.get("phone_no", user.phone_db)
            user.country_db = request.POST.get("country", user.country_db)
            user.state_db = request.POST.get("state", user.state_db)
            user.city_db = request.POST.get("city", user.city_db)
            
            courses = request.POST.getlist("courses")
            user.courses_db = ",".join(courses) if courses else "" 
            
            hobbies = request.POST.getlist("hobbies")
            user.hobbies_db = hobbies if hobbies else []

            if "avatar" in request.FILES:  
                user.file_db = request.FILES["avatar"]
            
            user.save()
            request.session['first_name'] = user.fname_db
            request.session['last_name'] = user.lname_db
            request.session['profile_picture'] = user.file_db.url if user.file_db else 'img/profile-placeholder.png'
            
            return redirect('profiledit') 

    context = {
        "fname": user.fname_db,
        "lname": user.lname_db,
        "gender": user.gender_db,
        "dob": user.dob_db.strftime("%Y-%m-%d") if user.dob_db else "",
        "email": user.email_db,
        "avatar": user.file_db.url if user.file_db else "img/profile-placeholder.png",
        "phone": user.phone_db,
        "country": user.country_db,
        "state": user.state_db,
        "city": user.city_db,
        "courses": user.courses_db.split(",") if user.courses_db else [],
        "hobbies": user.hobbies_db,
    }

    return render(request, "profile-edit.html", {"context": context, 'user_email': user_email})


def changepass(request):
    error_messages={}
    user_email = request.session.get('logged_user')
    if not user_email:
        messages.error(request, "Please log in to change your password.")
        return redirect('login') 
    if request.method == "POST":
        old_pass=request.POST.get("old_password")
        new_pass=request.POST.get("new_password")      
        try:
            user_pass = Studentsdbase.objects.get(password_db=old_pass)
            print(new_pass)
            user_pass.password_db= new_pass
            # print(user_pass)
            user_pass.save()
            request.session['new_password'] = new_pass
            return redirect('login')
        except :
            error_messages['pass_error'] = 'Invalid Password. Please try again.'
            print("error_messages")
    context = {
        'user_email': user_email,
        'user_first_name': request.session.get('first_name', 'User'),
        'user_last_name': request.session.get('last_name', ''),
        'user_img': request.session.get('profile_picture', 'img/profile-placeholder.png')
    }
    return render(request,"changepass.html",{'errors' : error_messages,'context' : context})


def log_out(request):
    request.session.flush()
    try:
        response=redirect('home')
    except Studentsdbase.DoesNotExist:
        return redirect('login') 
    response.delete_cookie('logged_user') 
    return response







