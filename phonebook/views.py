from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import *

@csrf_exempt
def getdata(request):
	name = request.GET['cname']
	num = request.GET['number']
	addr = request.GET['address']
	user = contact(contact_name = name, number = num, address = addr)
	user.save()
	return render(request, 'phonebook/index.php')

@csrf_exempt
def gendata(request):
	number = request.GET['number']
	user = contact.objects.all()
	flag = 0
	for i in range(contact.objects.count()):
		if number == user[i].number:
			name = user[i].contact_name
			address = user[i].address
			flag = 1
	if flag == 1:
		context = {'name' : name, 'number' : number, 'address' : address}
		return render(request, 'phonebook/disp.html', context)
	else:
		raise Http404("No such number exists!!!")