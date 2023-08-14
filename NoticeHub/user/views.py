from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Notice

def all_notices(request):
	allnotices = Notice.objects.all()
	context = {'result':allnotices}
	return render(request,'user/notice.html',context)

def home(request):
	context = {}
	return render(request,'user/home.html',context)

def aboutUs(request):
	context = {}
	return render(request,'user/aboutUs.html',context)
