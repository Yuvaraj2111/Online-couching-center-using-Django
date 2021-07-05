from django.shortcuts import render
from .models import Admin,Subject,User_account
# Create your views here.
# admin login page
def home(request):
	if request.method=='POST':
		user=request.POST['usr']
		password=request.POST['password']
		if Admin.objects.filter(name=user).exists():
			a=Admin.objects.get(name=user)
			if a.password==password:
				return render(request,'admin_home.html')
			else:
				return render(request,'admin.html',{'msg':'incorrect password'})
		else:
			return render(request,'admin.html',{'msg':'admin not found'})
	else:
		return render(request,'admin.html')
#page to open link in admin home

def adminhome(request,i):
	# for admins
	if i=='admin':
		c=[Admin.objects.all()]
		return render(request,'admin_add.html',{'ads':c})
	# for subjects
	elif i=='subject':
		a=[Subject.objects.all()]
		b=set()
		for i in a:
			for x in i:
				b.add(x.name)
		return render(request,'sub.html',{'s':b})
	# for students
	elif i=='student':
		c=[User_account.objects.all()]
		return render(request,'student.html',{'s':c})
	else:
		return render(request,'admin.html')

#for delete one admin

def admin_del(request,j):
	Admin.objects.get(name=j).delete()
	return render(request,'admin_add.html',{'msg':'one admin deleted'})

#to create admin
def add(request):
	if request.method=='POST':
		user=request.POST['usr']
		password=request.POST['password']
		cp=request.POST['confirm']
		if Admin.objects.filter(name=user).exists():
			return render(request,'create_admin.html',{'msg':'admin name already exists'})
		else:
			if cp==password:
				Admin.objects.create(name=user,password=password)
				return render(request,'create_admin.html',{'msg':'admin successfully added'})
			else:
				return render(request,'create_admin.html',{'msg':'password mismatch'})
	else:
		return render(request,'create_admin.html')
#to enter subject

# student details page


