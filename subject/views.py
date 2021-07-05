from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Subject
# Create your views here.a
def add_subject(request):
	if request.method=='POST':
		sub=request.POST['sub']
		detail=request.POST['detail']
		content=request.POST['content']
		try:
			video=request.FILES['video']
		except:
			video=''
		try:
			file=request.FILES['pdf']
		except:
			file=''
		
		if video!='':
			vid_path='/media/video/'+str(video.name)
			if Subject.objects.filter(video=vid_path).exists():
				pass
			else:
				vid =FileSystemStorage(location='media/video')
				vid.save(video.name, video)			
		else:
			vid_path=''
		if file!='':
			doc_path='/media/document/'+str(file.name)
			if Subject.objects.filter(pdf=doc_path).exists():
				pass
			else:
				pdf =FileSystemStorage(location='media/document')
				pdf.save(file.name, file)

		else:
			doc_path=''
		if sub!='':
			Subject.objects.create(name=sub,description=detail,content=content,video=vid_path,pdf=doc_path)
			return render(request,'add-sub.html',{'msg':sub+' added successfully'})
		else:
			return render(request,'add-sub.html',{'msg':'Subject cannot be empty'})
		
	else:
		return render(request,'add-sub.html')

def display(request):
	a=[Subject.objects.filter(name='')]
	l=set()
	d=set()
	for x in a:
 		for i in x:
 			s=i.name
 			l.add(i.video)
 			d.add(i.pdf)
	# format=a.video.split('.')[-1]
	return render(request,'display_video.html',{'video':l,'doc':d,'sub':s})