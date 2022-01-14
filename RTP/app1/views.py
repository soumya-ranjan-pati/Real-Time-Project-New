from django.shortcuts import render
from app1.forms import RegistrationForm

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

        else:
            return render(request,'app1_temp/Registration.html',{'form':rf})
    else:
        return render(request,'app1_temp/Registration.html',{'form':rf})
