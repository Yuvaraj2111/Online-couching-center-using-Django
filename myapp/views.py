from django.shortcuts import render
from .models import User_account,Staff,Contact,Enroll
# Create your views here.
def logout(request):
	return render(request,'login.html',{'result':'logout successfully'})

def home(request,i):
	a=User_account.objects.get(user=i)
	return render(request,'index.html',{'u':a})

def enroll(request,i,j):
	a=User_account.objects.get(user=i)
	Enroll.objects.create(user=i,subject=j)
	return render(request,'courses.html',{'u':a,'msg':j+' course added successfully'})

def about(request,j):
	c=User_account.objects.get(user=j)
	return render(request,'about.html',{'u':c})

def contact(request,i):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		email=request.POST['email']
		ph=request.POST['ph']
		m=request.POST['msg']
		a=User_account.objects.get(user=i)
		Contact.objects.create(fname=fn,lname=ln,email=email,phone=ph,msg=m)
		return render(request,'contact.html',{'u':a,'result':'contact added successfully'})
	else:
		a=User_account.objects.get(user=i)
		return render(request,'contact.html',{'u':a})

def admission(request,i):
	a=User_account.objects.get(user=i)
	return render(request,'admission.html',{'u':a})

# def pay(request):
# 	return render(request,'pay.html')

def cs(request,i,j):
	a=User_account.objects.get(user=i)
	return render(request,'course_single.html',{'u':a,'sub':j})

def course(request,i):
	a=User_account.objects.get(user=i)
	return render(request,'courses.html',{'u':a})

def login(request):
	if request.method=="POST":
		user=request.POST['username']
		ps=request.POST['password']
		if User_account.objects.filter(user=user).exists():
			c=User_account.objects.get(user=user)
			if c.password==ps:
				return render(request,'index.html',{'result':user,'u':c})
			else:
				return render(request,'login.html',{'result':'password incorrect','user1':user})
		else:
			return render(request,'login.html',{'result':"username doesn't exists"})
	else:
		return render(request,'login.html')

def register(request):
	if request.method=="POST":
		name=request.POST['name']
		user=request.POST['usr']
		email=request.POST['email']
		phone=request.POST['phone']
		ps=request.POST['password2']
		confirm=request.POST['confirm']
		if ps==confirm:
			if User_account.objects.filter(user=user).exists():
				return render(request,'register.html',{'result':'username already exists'})
			elif User_account.objects.filter(email=email).exists():
				return render(request,'register.html',{'result':"email already exists",'usr':user})
			elif len(phone)!=10 :
				return render(request,'register.html',{'result':"INVALID PHONE NUMBER",'usr':user, 'email':'email'})
			else:
				a=User_account.objects.create(name=name, user=user, email=email, phone=phone, password=ps)
				a.save()
				return render(request,'login.html',{'result':user+" created successfully",'usr':user})
		else:
			return render(request,'register.html',{'result':"password mismatch",'usr':user,'email':email})
	else:
		return render(request,'register.html')