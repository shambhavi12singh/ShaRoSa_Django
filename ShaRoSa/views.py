from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from ShaRoSa.models import *
import sys
def home(request):
    return render(request,"Home.html")
def log(request):
    try:
        if request.method=="POST":
            nm=request.POST['name']
            ml=request.POST['mail']
            pass2=request.POST['passwrd']
            s=ShaRoSa(name=nm,mail=ml,passwrd=pass2)
            s.save()
            return render(request,'Signup_s.html')  
        else:    
            return render(request,'login.html')
    except Exception as e:    
        return HttpResponse(e)
def log1(request):
    try:
        if request.method=='POST':
            ml=request.POST['mail']
            pass2=request.POST['passwrd']
            s=ShaRoSa.objects.get(mail=ml,passwrd=pass2)
            request.session['Username']='Guest'
            return render(request,'log_s.html')
        else:
             return render(request,'log_f.html')        
    except Exception as e:
        return render(request,'log_f.html') 
def about(request):
    return render(request,"about.html")
def menu(request):
    if 'Username' in request.session.keys():
        return render(request,"menu.html")
    else:
        return render(request,'acc_den.html')
    
def order(request):
    if 'Username' in request.session.keys():
        return render(request,"success.html")
    else:
        return render(request,'acc_den.html')
    
def book(request):
    if 'Username' in request.session.keys():
        if 'Room' in request.session.keys():
            return render(request,"ralb.html")
        else:
            return render(request,"book.html")
    else:
        return render(request,'acc_den.html')
def V1f(request):
    i='Full Plate SHAHI PANEER'
    c='460'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def V1h(request):
    i='Half Plate SHAHI PANEER'
    c='230'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def V2f(request):
    i='Full Plate SHAROSA SPECIAL CURRY'
    c='680'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def V2h(request):
    i='Half Plate SHAROSA SPECIAL CURRY'
    c='340'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def V3f(request):
    i='Full Plate LABABDAR PANEER'
    c='360'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def V3h(request):
    i='Half Plate LABABDAR PANEER'
    c='180'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def N1f(request):
    i='Full Plate EGG-CURRY'
    c='320'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def N1h(request):
    i='Half Plate EGG-CURRY'
    c='160'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def N2f(request):
    i='Full Plate SHAROSA SPECIAL CHICKEN'
    c='780'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def N2h(request):
    i='Half Plate SHAROSA SPECIAL CHICKEN'
    c='390'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def N3f(request):
    i='Full Plate HANDI CHICKEN'
    c='420'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def N3h(request):
    i='Half Plate HANDI CHICKEN'
    c='210'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D1f(request):
    i='250 ml ANTIQUITY'
    c='680'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D1h(request):
    i='750 ml ANTIQUITY'
    c='1455'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D2f(request):
    i='250 ml BLACK DOG'
    c='895'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D2h(request):
    i='750 ml BLACK DOG'
    c='1790'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D3f(request):
    i='250 ml 100 PIPERS'
    c='850'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D3h(request):
    i='750 ml 100 PIPERS'
    c='2040'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D4f(request):
    i='250 ml BACARDI WHITE RUM'
    c='590'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D4h(request):
    i='750 ml BACARDI WHITE RUM'
    c='1580'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def D5f(request):
    i='250 ml TEQUILA LEY.925'
    c='13000'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')   
def D5h(request):
    i='750 ml TEQUILA LEY.925'
    c='26000'
    s=Bill(item=i,charge=c)
    s.save()
    return render(request,'success.html')
def B1(request):
    i='BACHELOR ROOM'
    c='5000'
    s=Bill(item=i,charge=c)
    s.save()
    request.session['Room']='Booked'
    return render(request,'booked.html')

def B2(request):
    i='COUPLE ROOM'
    c='7500'
    s=Bill(item=i,charge=c)
    s.save()
    request.session['Room']='Booked'
    return render(request,'booked.html')

def B3(request):
    i='SUITE'
    c='10000'
    s=Bill(item=i,charge=c)
    s.save()
    request.session['Room']='Booked'
    return render(request,'booked.html')

def CO(request):
    if 'Username' in request.session.keys():
        s=Bill.objects.all()
        sum1=Bill.objects.aggregate(Sum('charge'))
        return render(request,'Bill.html',{'s':s,'sum':sum1})
    else:
        return render(request,'acc_den.html')

def dev(request):
    return render(request,'devs.html')

def ad(request):
    return render(request,'acc_den.html')
def Logout(request):
    if 'Username' in request.session.keys():
        del request.session['Username']
        del request.session['Room']
        Bill.objects.all().delete()
        return redirect('/ShaRoSa/home')
    else:
        return redirect('/ShaRoSa/home')
def ralb(request):
    return render(request,'ralb.html')