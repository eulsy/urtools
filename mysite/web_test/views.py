# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

from .data_format import dir_info

dir_config = {
"D:\\build" : 1,
"D:\\router" : 2
}


		

		

		
		
def index(request):
	if request.method == 'GET':
		data = []
		for i in dir_config:
			d = dir_info(i, dir_config[i])
			data.append({"data":d.data, "path": i})
		print(data)
		return render(request, 'web_test/templates/index.html', {'dir_info': data, "title": "code list"})
	else:
		return HttpResponseNotFound("Can't find %s request!"%(request.method))
		
def del_code(request):
	if request.method == 'POST':
		print(request.POST)
		return HttpResponse("1111t!")
	else:
		return HttpResponseNotFound("Can't find %s request!"%(request.method))
	
