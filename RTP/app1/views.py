from django.shortcuts import render,redirect
from app1.forms import RegistrationForm
from app1.models import RegistrationModel
from django.contrib.messages import success

# Create your views here.
def showindex(request):
    return render(request,'app1_temp/main.html')
#create a app and write the html it is the advantages is this total app operation wil be store in this app.
#after some issue u create a new aap then no problem u create a another aap and work ur operation.


def registration(request):
    rf=RegistrationForm(request.POST)
    if request.method == 'POST':
        if rf.is_valid():
            #rf.otp = 5475
            #rf.status = 'pending'#Not Write status in this place means this status write in default in models thats way
            rf.save()
            return redirect('user_otp')

        else:
            return render(request,'app1_temp/Registration.html',{'form':rf})
    else:
        return render(request,'app1_temp/Registration.html',{'form':rf})


def userotp(request):
    return render(request,'app1_temp/otp.html')


def validate_otp(request):#get--it will return only one object
    try:
        result = RegistrationModel.objects.get(contact=request.POST.get('t1'),otp=request.POST.get('t2'))
        #print(result.status)
        if result.status == 'pending':
            result.status == 'approved'#updating the record
            result.save()
            success(request,'Thank You For Registration ')
            return redirect('conformation')
        elif result.status == 'approved':
            success(request,'Your Registration Is Already Approved')
            return redirect('conformation')

    except RegistrationModel.DoesNotExist:
        message='Sorry This User Is Invalid'
        return render(request,'app1_temp/otp.html',{'message':message})



def conformation(request):
    return render(request,'app1_temp/conformation.html')


def login(request):
    return render(request,'app1_temp/login.html')