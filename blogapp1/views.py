from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogapp1.models import Doginfo
from django.db.models import Q
from blogapp1.forms import empformclass,Doginfoclass,UserRegister
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def about(request):
    return redirect("/contact")

def contact(request):
    return HttpResponse("I'm Amay")

def job(request):
    return HttpResponse("I'm a Python Programmer and Web Developer")

def info(request):
    return HttpResponse("I love you baby")

def stud(request,sid):
    print("Stud id is:",sid)
    return HttpResponse("Stud id is:"+ sid)

def add(request,x,y):
    print("First Number is:",x)
    print("second Number is:",y)
    z=int(x)+int(y)
    print("Addition=",z)
    return HttpResponse("Addition="+str(z))

def hello(request):
    print("Hello from view function")
    return HttpResponse(render(request,"hello.html"))

def hyedad(request):
    d1={"name":"Amay"}
    d1["x"]=50
    d1["y"]=30
    d1["w"]=70
    d1["z"]=[10,20,30,50,60,70]
    print(d1)
    return HttpResponse(render(request,"hello.html",d1))

def code(request):

    return HttpResponse(render(request,"code.html"))

def test(request):
    return HttpResponse(render(request,"test.html"))

def lstat(request):
    return render(request,"learnstatic.html")

def dogn(request):
    user_id=request.user.id
    # print("User logged in:User",user_id)
    if request.method=="POST":
        bn=request.POST["bname"]
        gd=request.POST["gend"]
        ag=request.POST["age"]
        vac=request.POST["vac"]
        pri=request.POST["price"]
    
        p=Doginfo.objects.create(breed_name=bn,gender=gd,age=ag,vaccine=vac,price=pri,uid=user_id)
        p.save()
        # return HttpResponse("Record inserted successfully")
        return redirect("/dashboard")
        
    else:
        return render(request,"dognation.html")

def dashboard(request):
    user_id=request.user.id
    # q=Doginfo.objects.all()
    q=Doginfo.objects.filter(uid=user_id)
    #print(qset)
    content={}
    content["data"]=q

    return render(request,"dashboard.html",content)

def edit(request,rid):
    #return HttpResponse("ID to be edited:"+rid)
    if request.method=="POST":
        # pass
        bn=request.POST["bname"]
        gd=request.POST["gend"]
        ag=request.POST["age"]
        vac=request.POST["vac"]
        pri=request.POST["price"]

        # print(bn)
        # print(gd)
        # print(ag)
        # print(vac)
        # print(pri)
        p=Doginfo.objects.filter(id=rid)
        p.update(breed_name=bn,gender=gd,age=ag,vaccine=vac,price=pri)
        
        return redirect("/dashboard")

        
        # p=Doginfo.objects.create(breed_name=bn,gender=gd,age=ag,vaccine=vac,price=pri)
        # p.save()
        # # return HttpResponse("Record inserted successfully")
        # return redirect("/dashboard") 
    else:
        p=Doginfo.objects.filter(id=rid) 
        content={}
        content["data"]=p
        return render(request,"edit.html",content)
        

def delete(request,rid):
    p=Doginfo.objects.filter(id=rid)
    # print(p)
    p.delete()
    #return HttpResponse("ID to be deleted:"+rid)
    return redirect("/dashboard")

def gender(request,gid):
    user_id=request.user.id
    # p=Doginfo.objects.filter(gender=gid)
    p=Q(gender=gid)
    q=Q(uid=user_id)
    r=Doginfo.objects.filter(p & q)
    # print(p)
    content={}
    # content["data"]=p
    content["data"]=r
    return render(request,"dashboard.html",content)

def vaccine(request,vid):
    p=Doginfo.objects.filter(vaccine=vid)
    # print(p)
    content={}
    content["data"]=p
    return render(request,"dashboard.html",content)

def price(request,a):
    if a=="1":
        p=Doginfo.objects.order_by("price")
    else:
        p=Doginfo.objects.order_by("-price")
    
    content={}
    content["data"]=p
    return render(request,"dashboard.html",content)

def filp(request,fid):
    if fid=="1":
        p=Doginfo.objects.filter(price__gt=20000) #for greater than
        # p=Doginfo.objects.filter(price__gte=20000) #for greater than equal to
        # p=Doginfo.objects.filter(price__gte=20000).order_by("price") #to display in Asc order
        # p=Doginfo.objects.filter(price__gte=20000).order_by("-price") #to display in Des order
    else:
        p=Doginfo.objects.filter(price__lt=20000) #for less than
        # p=Doginfo.objects.filter(price__lte=20000) #for less than equal to
    
    content={}
    content["data"]=p
    return render(request,"dashboard.html",content)

def multifilter(request):
    if request.method=="POST":
        gn=request.POST["gend"]
        vn=request.POST["vac"]
        # print(gn,vn)
        q1=Q(gender=gn)
        q2=Q(vaccine=vn)
        p=Doginfo.objects.filter(q1 & q2)

        content={}
        content["data"]=p
        return render(request,"dashboard.html",content)
    
# Django Forms    

def django_form(request):

    if request.method=="POST":
        nm=request.POST["empname"]
        mb=request.POST["mobile"]
        dp=request.POST["department"]
        dt=request.POST["doj"]

        print(nm)
        print(mb)
        print(dp)
        print(dt)
        return redirect("/djforms")


    else:
        dfobj=empformclass()
        # print(dfobj)
        content={}
        content["form"]=dfobj
        return render(request,"empform.html",content)
    

def modelform(request):

    if request.method=="POST":
        # pass
        mof=Doginfoclass(request.POST)
        if mof.is_valid():
            mof.save()
            return redirect("/dognationmof")
        

    else:
        mof=Doginfoclass()
        # print(mof)
        content={}
        content["mform"]=mof
        return render(request,"dognationmodel.html",content)
    
def userregform(request):

    if request.method=="POST":
        userrf=UserRegister(request.POST)
        # print(userrf)
        print(userrf.is_valid())
        if userrf.is_valid():
            userrf.save()
            content={"msg":"User Registered Successfully"}
            return render(request,"userlogin.html",content)
            # return redirect("/admin/login/?next=/admin/") use this for redirecting to admin login page directly after login

    else:
        # userrf=UserCreationForm() use this for standard User Creation Form
        # print(userrf)
        userrf=UserRegister()
        # print(userrf)
        content={"regform":userrf}
        return render(request,"register.html",content)
    
def user_login(request):
    if request.method=="POST":
        userlog=AuthenticationForm(request=request,data=request.POST)
        # print(userlog)
        if userlog.is_valid():
            uname=userlog.cleaned_data["username"]
            upass=userlog.cleaned_data["password"]
            # print(uname,upass)
            usr=authenticate(username=uname,password=upass)
            if usr:
                login(request,usr)
                return redirect("/dashboard")
        

    else:
        userlog=AuthenticationForm()
        # print(userlog)
        content={"form":userlog}
        return render(request,"login.html",content)
    

def setcookie(request):
    res=render(request,"setcookie.html")
    res.set_cookie("name","Amay")
    res.set_cookie("roll_no",14)
    res.set_cookie("place","Mumbai")
    return res

def getcookie(request):
    nm=request.COOKIES["name"]
    rn=request.COOKIES["roll_no"]
    pl=request.COOKIES["place"]
    content={"n":nm,"r":rn,"p":pl}
    return render(request,"getcookie.html",content)

def setsession(request):
    request.session["name"]="Dazzy"
    request.session["place"]="Panvel"
    return render(request,"setsession.html")

def getsession(request):
    content={}
    content["n"]=request.session["name"]
    content["p"]=request.session["place"]
    return render(request,"getsession.html",content)



    

