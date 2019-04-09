from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import uni
from  django.db.models import Q




def index(request):
	
	return render(request,'sit/index.html',{})


def index1(request):
    
    return render(request,'sit/index1.html',{})




def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)



        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')




    else:
        form = UserCreationForm()
          
    context = { 'form' : form }

    return render(request,'registration/sign.html', context)





def logout1(request):
    logout(request)
    return redirect('index1')

def coll(request):
    if request.method =='POST':
        serch = request.POST['srh']
        if serch:
            match = uni.objects.filter(Q(cname__icontains=serch))
            if match:
                return render(request,'sit/coll.html', {'sr':match})
  
              
    return render(request,'sit/coll.html',{'coll':coll})
	


def indo(request):
    return render(request,'sit/indo.html')