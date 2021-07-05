from django.template.defaulttags import register 
from django.shortcuts import render
from .models import User_account, Enroll, Subject
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
# Create your views here.

def show(request,a):
	u=User_account.objects.get(user=a)
	s=[Enroll.objects.filter(user=a)]
	sub=set()
	for i in s:
		for j in i:
			sub.add(j.subject)
	return render(request,'user_view.html',{'name':u.name,'user':u.user,'email':u.email,'phone':u.phone,'subject':sub})

def display(request,i,j):
	u=User_account.objects.get(user=i)
	s=[Subject.objects.filter(name=j)]
	vid=set()
	doc=set()
	dec=[]
	con=[]
	for i in s:
		for x in i:
			if x.video=='':
				pass
			else:
				vid.add(x.video)
			if x.pdf=='':
				pass
			else:
				doc.add(x.pdf)
			sub=x.name
			if x.content=='':
				pass
			else:
				con.append(x.content)
			if x.description=='':
				pass
			else:
				dec.append(x.description)
	for j in dec:
		d=j
	for j in con:
		c=j
	vid=list(vid)
	doc=list(doc)
	print(vid)
	pg=request.GET.get('q', 1)
	page = Paginator(vid, 1)
	try:
		ab=page.page(pg)
	except PageNotAnInteger:
		ab=page.page(1)
	except EmptyPage:
		ab=page.page(page.num_pages)
	return render(request,'study.html',{'p':ab,'u':u,'sub':sub,'doc':doc,'description':d,'content':c})

@register.filter
def set_one(x):
	x=1
	return x

@register.filter
def inc(x):
	x+=1
	return x

def certificate(request,i,j):
	return render(request,'Certificate.html',{'name':i,'enrolled_course':j,'sign':i})