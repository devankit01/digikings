from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
import uuid

from DigiKings.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# For html content sending
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                email = request.POST['email']
                user = User.objects.filter(email=email)
                if len(user) == 0:
                    raise User.DoesNotExist
                return render(request, 'Users/signup.html', {'msg': 'Email already exists 🔑', 'c': 'red'})
            except User.DoesNotExist:
                # user = '@'+request.POST['email']
                user = email
                user_obj = User.objects.create_user(
                    first_name=request.POST['first_name'], last_name=request.POST['first_name'], username=user, password=request.POST['pass1'], email=request.POST['email'])
                print(user_obj)

                # User set to is_active = False

                auth_token = str(uuid.uuid4())
                print(type(auth_token))

                user_obj.save()


                new_prof = Profile(username=user_obj,phone=request.POST['phone'], gender="", auth_token = auth_token , is_verified = False)
                new_prof.save()

                # send(user_obj)

                # Send Email

                send_token_link(request, email,auth_token)

                return redirect('token_send')

        else:
            return render(request, 'users/signup.html', {'msg': "Password do not matched ❌"})
    else:
        return render(request, 'users/signup.html')

def token_send(request):
    return render(request, 'users/token.html')


def send_token_link(request,email,token):
    subject = "Account Verfication"

    message = "Hello User, Please click on the link to verify your account " +  request.scheme + "://" + request.META['HTTP_HOST'] + "/accounts/verify/" + token
    recipient = [email]
    print(message)
    try:
        send_mail(subject, message, EMAIL_HOST_USER , recipient, fail_silently = True)
    except Exception as e:
        print(e)

def verify_token(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        user_obj = User.objects.get(username=profile_obj.username)
        print(profile_obj)
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            try:
                send(user_obj)
            except:
                pass
            return render(request, 'users/verify.html')
        return HttpResponse('<h1>Error 400</h1>')
    except Exception as e:
        print(e)
        return HttpResponse('Error 400 ')

def send(user_obj):
    subject, from_email = 'Welcome', EMAIL_HOST_USER
    html_content = render_to_string(
        'Users/welcome_email.html', {'i': user_obj})  # render with dynamic value
    # Strip the html tag. So people can see the pure text at least.
    text_content = strip_tags(html_content)
    # create the email, and attach the HTML version as well.
    emails = user_obj.email
    to = []
    to.append(emails)

    # print(i.username.email)
    print(to)
    msg = EmailMultiAlternatives(
        subject, text_content, 'Welcome' + EMAIL_HOST_USER, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('Email ok')



def signin(request):
    if request.method == "POST":
        try:
            uname = request.POST['email']
            pwd = request.POST['password']
            print(uname, pwd)

            uid = User.objects.get(username=uname)
            profile = Profile.objects.get(username=uid)
            if profile.is_verified:

                user_authenticate = auth.authenticate(username=uname, password=pwd)
                print(user_authenticate)
                if user_authenticate is not None:
                    if user_authenticate.is_staff:
                        auth.login(request, user_authenticate)
                        request.session['username'] = uname
                        # Code changed
                        return redirect('profile')
                    else:
                        auth.login(request, user_authenticate)
                        request.session['username'] = uname
                        return redirect('profile')
                else:
                    print('Login Failed')
                    return render(request, 'users/signin.html', {"msg": "Invalid Credentials"})
            else:
                return render(request, 'users/signin.html', {"msg": "Please Verify your Account ‼"})

        except:
            return render(request, 'users/signin.html', {"msg": "No any account "})

    else:
        return render(request, 'users/signin.html')

def profile(request):
    if checkLogin(request):
        user = get_object_or_404(User, username=request.user)
        user = get_object_or_404(Profile, username=user)
    
        if (user.gender=='' )and( user.pin_code and user.country and user.location) is None:
            Profile_status=True
        else:
            Profile_status=False
     
        return render(request, 'Users/profile.html',{'user': user,'status':Profile_status})
    return redirect('signin')

def logout(request):
    
    uid = User.objects.get(username=request.user)
    print(uid)
    auth.logout(request)

    if request.session.has_key('username'):
        del request.session['username']
    else:
        pass

    return redirect('signin')


def checkLogin(request):
    if request.session.has_key('username'):
        return True
    else:
        print('No Login')
        return False







# Admin Panel Code
def adminPanelHome(request):
    return render(request, 'adminPanel/home.html')

def Profile_Completed(request):
    if checkLogin(request):
        user = get_object_or_404(User, username=request.user)
        user = get_object_or_404(Profile, username=user)
        if (user.gender=='' )and( user.pin_code and user.country and user.location) is None:
            if request.method=="POST":
                try:
                    Gender=request.POST['Gender']
                    pin_Code=request.POST['pin_code']
                    country=request.POST['Country']
                    Location=request.POST['Location']
                    user.location=Gender
                    user.pin_code=pin_Code
                    user.country=country
                    user.location=Location
                    user.save()
                    return redirect('profile')
                except:
                    return redirect('profile')
            else:
                return redirect('Profile')