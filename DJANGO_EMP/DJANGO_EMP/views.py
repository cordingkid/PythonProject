from django.shortcuts import render
from django.http import HttpResponse
from DJANGO_EMP.dao_emp import DaoEmp
from boto.mturk.question import QuestionForm


def index(request):
    return HttpResponse("<h1>Hello Django!!!!!!</h1>")


def empList(request):
    de = DaoEmp()
    myList = de.selectList()
    return render(request, "empList.html", {"list":myList})

def emp_detail(request):
    e_id = request.GET.get('e_id', None)
    de = DaoEmp()
    empOne = de.selectOne(e_id)
    return render(request, "emp_detail.html", {"empOne":empOne})

def emp_mod(request):
    e_id = request.GET.get('e_id', None)
    de = DaoEmp()
    empOne = de.selectOne(e_id)
    return render(request, "emp_mod.html", {"empOne":empOne})

def emp_mod_act(request):
    e_id = request.POST.get('id')
    e_name = request.POST.get('name')
    sex = request.POST.get('sex')
    addr = request.POST.get('addr')
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    return render(request, "emp_mod_act.html", {"cnt":cnt})

def emp_add(request):
    return render(request, "emp_add.html")

def emp_add_act(request):
    e_id = request.POST.get('id')
    e_name = request.POST.get('name')
    sex = request.POST.get('sex')
    addr = request.POST.get('addr')
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    return render(request, "emp_add_act.html", {"cnt":cnt})

def emp_del_act(request):
    e_id = request.POST.get('id')
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    return render(request, "emp_del_act.html", {"cnt":cnt})