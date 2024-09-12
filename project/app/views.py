from django.shortcuts import render

# Create your views here.
def set(request):
    # my_list1 = {'id':1,'name':'priya','city':'Bhopal'}
    # my_list2 = {'id':2,'name':'suriya','city':'indore'}
    # my_list = [my_list1,my_list2]
    # request.session['data']=my_list
    request.session['name']='Neeraj'
    request.session['city']='Bhopal'
    request.session['roll']='101'

    return render(request,'set.html')

def get(request):
    data1 = request.session.get('data','Guest')
    return render(request,'get.html',{"name":data1})

def delete(request):
    print(request.session)

    if 'name'in request.session:
        x= request.session['data']
        # del request.session['data']
        # request.session.fulsh()
    #  request.session.flush()
    # return render(request,'delete.html')    

