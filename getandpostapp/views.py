from django.shortcuts import render
from django.http import HttpResponse
def getinput(request):
    return render(request,'getinut.html')
def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=="GET":
        s1=request.GET["t1"]
        s2=request.POST['t2']
        try:
            i=int(s1)
            j=int(s2)
            k=i+j
            return HttpResponse("<html><body bgcolor=blue><h1>sum is :"+str(k)+"</h1></body></html>")
        except(ValueError):
            return  render(request,'getinput.html')
    else:
        s1=request.post("t1")
        s2=request.post("t2")
        try:
            i=int(s1)
            j=int(s2)
            k=i+j
            return HttpResponse("<html><body bgcolor=cyan<h1><sum is:"+str(k)+"</h1><body></html>")
        except(ValueError):
            return render(request,'post.html')

