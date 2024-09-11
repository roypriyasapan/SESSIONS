from django.shortcuts import render

# Create your views here.
def set(request):
    my_list1 = {'id':1,'name':'priya','city':'Bhopal'}
    my_list2 = {'id':2,'name':'suriya','city':'indore'}
    my_list = [my_list1,my_list2]
    request.session['data']=my_list

    return render(request,'set.html')

def get(request):
    data1 = request.session.get('data','Guest')
    return render(request,'get.html',{"name":data1})