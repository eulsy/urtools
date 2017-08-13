# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os
def get_size(path):

	try:path = path.path
	except:pass
	if os.path.isfile(path):
		return os.path.getsize(path)
	else:
		return sum(map(get_size, os.scandir(path)))

def index(request):
	dir_info = {}
	for i in os.scandir("D:\\build"):
		dir_info[i.name] = get_size(i.path)
	return render(request, 'web_test/templates/index.html', {'dir_info': dir_info, "title": "code list"})