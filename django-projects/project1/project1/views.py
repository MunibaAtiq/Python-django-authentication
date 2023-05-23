# from django.http import HttpResponse
# from django.shortcuts import render

# def homePage(request):
#     data ={
#         'title':'index Page',
#         'clist':['PHP','Java','Django'],
#         'marks':400,
#     }
#     return render(request,"index.html",data)

# def aboutUs(request):
#     return HttpResponse("<h1>Welcome to Project1</h1>")

# def course(request):
#     return HttpResponse("Welcome to Python Course")

# ------------------CLASS 2----------------------
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm    
from django.contrib.auth import logout

def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
        else:
            return render(request,'signup.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})  
    
def signout(request):
    logout(request)
    return redirect('/')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request,'Login.html',{'form':form,'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
