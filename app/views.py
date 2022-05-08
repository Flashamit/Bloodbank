from .models import *
from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request, 'home.html')  
def bloodbdetails(request):
    data = Bloodbank.objects.all()
    mydata = {'bbform':data}
    return render(request, 'bloodbdetails.html',context=mydata)
def donordata(request):
    data = Donor.objects.all()
    mydata = {'mydata':data}
    return render(request, 'donordata.html',context=mydata)
def reciverdata(request):
    data = Receiver.objects.all()
    mydata = {'mydata':data}
    return render(request, 'reciverdata.html',context=mydata)                 
def logins(request):
    if request.method=='POST':
        uname = request.POST['uname']
        passwd = request.POST.get('passwd')
        data = MyUser.objects.filter(username__iexact=uname).filter(password__iexact=passwd)
        if data:
            for i in data:
                request.session['utype']=i.usertype
                request.session['user_name']=f"{i.firstname} {i.lastname}"
            return redirect('home')
        else:
            return HttpResponse("<h2>Invailid Cridentails..</h2>")
    else:
        return render(request, 'login.html')
def logouts(request):
    logout(request)
    return redirect('home')             
def donorlist(request):
    data = Donor.objects.all()
    mydata={'dform':data}
    return render(request, 'donorlist.html',context=mydata)  
def reciverlist(request):
    data = Receiver.objects.all()
    mydata={'rform':data}
    return render(request, 'donorlist.html',context=mydata)
def complaintlist(request):
    data = Complaint.objects.all()
    return render(request, 'complaintdata.html',context={'mydata':data})      
class Ragistration(View):
    def get(self, request):
        forms = UserForm()
        return render(request, 'register.html', {'myforms':forms})
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')    
def search(request):
    if request.method=='POST':
        bg = request.POST['bg']
        ct = request.POST.get('ct')
        if bg and not ct :
            data = Donor.objects.filter(bloodgroup__iexact=bg)
        elif ct and not bg :
            data = Donor.objects.filter(city__iexact=ct)
        elif bg and ct :
            data = Donor.objects.filter(bloodgroup__iexact=bg).filter(city__iexact=ct)
        else:
            data= Donor.objects.all()
        return render(request ,'donorlist.html',context={'mydata':data})
    else:
        return render(request,'search.html')                   
class BForm(View):
    def get(self,request):
        form=BBForm()
        return render(request, 'bbform.html',context={'bbform':form})  
    def post(self, request):
        form = BBForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')       
class DonerForm(View):
    def get(self, request):
        dform=DForm()
        return render(request,'donerform.html',context={'mydata':dform})
    def post(self,request):
        dform=DForm(request.POST)
        if dform.is_valid():
            dform.save()
        return redirect('home')     
class ReciverForm(View):
    def get(self, request):
        rform=RForm()
        return render(request,'reciverform.html',context={'reciverform':rform})
    def post(self,request):
        rform=RForm(request.POST)
        if rform.is_valid():
            rform.save()
        return redirect('home')
class ComplaintForm(View):
    def get(self, request):
        cform=CForm()
        return render(request,'complaintform.html',context={'complaintform':cform})
    def post(self,request):
        rform=CForm(request.POST)
        if rform.is_valid():
            rform.save()
        return redirect('home')                 
class UpdateBB(View):
    def get(self,request,pk):
        obj=get_object_or_404(Bloodbank,bloodbankid=pk)
        bform=BBForm(instance=obj)
        return render(request,'updatebb.html',{'myform':bform})
    def post(self,request,pk):
        obj=get_object_or_404(Bloodbank,bloodbankid=pk)
        bform=BBForm(request.POST,instance=obj)
        if bform.is_valid():
            bform.save()
            return redirect('home')  
class DeleteBB(View):
    def get(self,request,pk):
        obj=get_object_or_404(Bloodbank,bloodbankid=pk)                         
        bform=BBForm(instance=obj)
        return render(request,'deletebb.html',{'myform':bform})
    def post(self,request,pk):
        obj=get_object_or_404(Bloodbank,bloodbankid=pk)
        obj.delete()
        return redirect('home')

        