from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
def user_register(request):
    if not request.user.is_authenticated:
        return render(request,'register.html')
    else:
        return redirect('dashboard')
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect('dashboard')

            else:
                return redirect('login')
        else:
            return render(request,'login.html')
    else:
        return redirect('dashboard')

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            roll_no = request.POST.get('roll_no')
            print(fname)
            print(lname)
            print(email)
            print(password)
            try:
                send_mail(
                    subject='Thank you for Registration on Voter App!!',
                    message= f'Your Username ={email} \n password={password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )
                User.objects.create_user(first_name=fname,last_name=lname,username=roll_no,email=email, password=password).save()
                print("Done")
                return JsonResponse({
                        'msg':'Register Successfully!!!!'
                    })
            except Exception as e:
                print(e)
                return JsonResponse({
                    'msg':e
                })
            try:
                send_mail(
                    subject='Thank you for Registration on Voter App!!',
                    message= f'Your Username ={email} \n password={password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )
                User.objects.create_user(first_name=fname,last_name=lname,username=roll_no,email=email, password=password).save()
                print("Done")
                return JsonResponse({
                        'msg':'Register Successfully!!!!'
                    })
            except Exception as e:
                print(e)
                return JsonResponse({
                    'msg':'Invalid Email ID!!'
                })
        else:
            return render(request,'login.html',{'error':'invalid Mail Id'})
    else:
        return redirect('dashboard')


def user_logout(request):
    logout(request)
    return redirect('login')