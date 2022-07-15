from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
import pandas as pd

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'main.html')
    else:
        return redirect('login')



def index(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')


def voters(request):
    if request.user.is_authenticated:
        cat = Category.objects.get(active=True)
        student = Student.objects.filter(category=cat)
        user = User.objects.get(id=request.user.id)
        try:
            votes = Vote.objects.get(user=user,category=cat)
            return render(request,'votes.html',{'cat':cat,'student':student,'vote':votes})
        except:
            return render(request,'votes.html',{'cat':cat,'student':student})
    else:
        return redirect('login')


def save_vote(request):
    if request.method == 'POST':
        print(request.POST.get('id'))
        print(request.POST.get('score'))
        stu = Student.objects.get(id=request.POST.get('id'))
        user = User.objects.get(id=request.user.id)
        print(stu)
        cat = Category.objects.get(category_name=stu.category)
        vote = Vote(user=user,name=stu.name,roll_no=stu.roll_no,category=cat,branch=stu.branch,score=request.POST.get('score'))
        vote.save()
        return redirect('index')
    else:
        return redirect('login')


def analysis(request):
    if request.user.is_authenticated:
        cat = Category.objects.all()
        return render(request,'analysis.html',{'cat':cat})
    else:
        return redirect('login')


def analysis_data(request, cat):
    if request.user.is_authenticated:
        vote = Vote.objects.filter(category=Category.objects.get(category_name=cat))
        q = vote.values('name', 'roll_no','score')
        df = pd.DataFrame.from_records(q)
        names = set(df.name)
        scores = []
        for data in list(names):
            print(sum(df[df.name==data].score.astype(int)))
            scores.append(sum(df[df.name==data].score.astype(int)))
        
        print(list(names))
        print(scores)
        return render(request,'all_analysis.html',{'labels':list(names),'scores':scores})
    else:
        return redirect('login')



def show_details(request,id):
    if request.user.is_authenticated:
        student = Student.objects.get(id=id)
        cat = Category.objects.get(category_name=student.category)
        try:
            votes = Vote.objects.get(user=request.user.id,name=student.name,category=cat)
            return render(request,'show_details.html',{"student":student,'votes':votes})
        except:
            return render(request,'show_details.html',{"student":student})
    else:
        return redirect('login')

