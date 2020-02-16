from django.shortcuts import render
from django.http import HttpResponse
from . models import *




# Create your views here.
def fn_home(request):
    return render(request,"home.html")

def fn_viewtower(request):
    return render(request,"viewtower.html")    

def fn_login(request):
    try:
        if request.method == 'POST':
            username   = request.POST['username']
            password   = request.POST['password']
            login_obj  = Login.objects.get(username=username)
            request.session['user_id']=login_obj.id
            
            if login_obj.password == password:
                if login_obj.role == 'admin':
                    return render(request,"menu.html")
                return render(request,"userhome.html")
            return HttpResponse('incorrect password')
        return render(request,"login.html")
    except Exception as e:
        print(e)
        return HttpResponse('incorrect username')
            
        
   

def fn_register(request):
    if request.method == 'POST':
        try:
            name    = request.POST['name']
            email = request.POST['email']
            mobile   = request.POST['mobile']
            username    = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            
            check_exist= Login.objects.filter(username=username).exists()
            if check_exist == False:
                login_obj = Login(username=username,password=password)
                print(login_obj)
                login_obj.save()
                if login_obj.id>0:
                    register_obj=Register(name=name,mobile=mobile,cpassword=cpassword,
                    email=email,fk_login=login_obj)
                    print(register_obj)
                    register_obj.save()
                    if register_obj.id>0:
                        return HttpResponse('Registered successfully')
                return HttpResponse('success')
            return HttpResponse('already exist')
            
        except Exception as e: 
            print(e)

            return HttpResponse('invalid') 
    return render(request,"register.html")



def fn_menu(request):
    return render(request,"menu.html")


def fn_showrack(req):
    try:
        rack_obj = Rack.objects.all()
        print(rack_obj)
        return render(req,"showrack.html",{'rackdata':rack_obj})
    except Exception as e:
        print(e)   

   
    

def fn_addrack(request):
    try:
        if request.method =="POST":
           rackname     = request.POST['rackname']
           qrcode        = request.POST['qrcode']
           rack_obj     = Rack(rack_name=rackname,qrcode=qrcode)
           rack_obj.save()
        #    print(rack_obj)
           if rack_obj.id > 0:
                return render(request,"addrack.html",{'msg':'Data entered'})
             
        return render(request,"addrack.html")
    except Exception as e:
        print(e)
        return HttpResponse('balance error')




def fn_addbay(request): 
    rack_obj = Rack.objects.all()
    return render(request,'addbay.html',{'rackdata':rack_obj}) 

    try: 
        # if request.method =="POST":
        rak_obj = request.POST['rakid']
        print(rak_obj)
           
       
        return render(request,"addbay.html") 
    except Exception as e: 
        print(e)

def fn_showbay(req):
    try:
        # bay_obj = Bay.objects.all()
        # print(bay_obj)
        return render(req,"showbay.html",)
    except Exception as e:
        print(e)  


def fn_addtower(request):
    try:
        # rack_obj = Rack.objects.all()
        # return render(request,'addbay.html',{'rackdata':rack_obj}) 
        # if request.method == "POST":
           
        #     towername     = request.POST['towername']
        #     print(towername)
            # towerlocation = request.POST['towerlocation']
            # qrcode        = request.POST['qrcode']
            # towercolor    = request.POST['towercolor']
            # towerheight   = request.POST['towerheight']
            # tower_obj     = Addtower(tower_name=towername,tower_location=towerlocation,qrcode=qrcode)
            # tower_obj.save()
            # print(tower_obj)
        return render(request,"addtower.html")
    except Exception as e:
        print(e)  

def fn_showtower(req):
    try:
        # tower_obj = Tower.objects.all()
        # print(tower_obj)
        return render(req,"showtower.html")
    except Exception as e:
        print(e)  



def fn_logout(request): 
    # del request.session['user_id'] 
    return render(request,'login.html')        