from django.shortcuts import render
from django.http import HttpResponse
from boto.mturk.question import QuestionForm
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from DJANGO_MVVM.dao_emp import DaoEmp
import json


def index(request):
    return render(request, "index.html")

@csrf_exempt
def ajax(request):
    menu = request.GET.get('menu',None)
    context = {"menu" : f"{menu}"}
    return JsonResponse(context)

@csrf_exempt
def ajax_empList(request):
    de = DaoEmp()
    myList = de.selectList()
    myJsonList = {
       "list" :  myList
    }
    return JsonResponse(myJsonList)

def ajax_emp_detail(request):
    e_id = request.GET.get('e_id', None)
    de = DaoEmp()
    empOne = de.selectOne(e_id)
    jsonEmp = {
        "emp" : empOne
    }
    return JsonResponse(empOne)


@csrf_exempt
def ajax_emp_mod(request):
    param = json.loads(request.body)
    
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    print(e_id,e_name,sex,addr)
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    print(cnt)
    return JsonResponse({"cnt":cnt})

@csrf_exempt
def ajax_emp_add(request):
    param = json.loads(request.body)
    
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    return JsonResponse({"cnt":cnt})

@csrf_exempt
def ajax_emp_del(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    return JsonResponse({"cnt":cnt})