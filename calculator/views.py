from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    result=None
    if request.method == 'POST':
       a = int(request.POST.get('Num1'))
       b = int(request.POST.get('Num2'))
       op = request.POST.get('Op')
       if op =='add':
           result = a+b
       elif op =='sub':
           result = a-b
       elif op =='mul':
           result = a*b
       elif op =='div':
           if b != 0:
               result = a/b
           else:
               error = "Cannot divide by zero"
       else:
           return render(request,'home.html',{'error':'error'})
       #return render(request,'home.html',{'result':result})  
       return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})
