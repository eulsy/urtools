# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

from .data_format import dir_info
import os, shutil

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
        return render(request, 'web_test/templates/index.html', {'dir_info': data, "title": "code list", "sep":os.sep})
    else:
        return HttpResponseNotFound("Can't find %s request!"%(request.method))
        
def del_code(request):
    if request.method == 'POST':
        print(request.POST)
        del_path = request.POST["path"]
        up_path = os.path.dirname(del_path)
        mid_path = os.path.join(up_path, "need_del")
        if os.path.isfile(del_path):
            if del_path != mid_path:os.rename(del_path,mid_path)
            os.remove(mid_path)
        elif os.path.isdir(del_path):
            if del_path != mid_path:shutil.move(del_path,mid_path)
            shutil.rmtree(mid_path)
        else:
            print("unknow file type")
        import time
        time.sleep(3)
        return HttpResponse("success")
    elif request.method == 'GET':
        data = []
        for i in dir_config:
            d = dir_info(i, dir_config[i])
            data.append({"data":d.data, "path": i})
        print(data)
        return render(request, 'web_test/templates/index.html', {'dir_info': data, "title": "code list", "sep":os.sep})
    else:
        return HttpResponseNotFound("Can't find %s request!"%(request.method))
    
