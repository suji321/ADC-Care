from django.contrib.auth import login, logout,authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import User

# Create your views here.
def register(request):
    return render(request, 'register.html')

class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'patregister.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loggedin')

class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'docregister.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loggedin')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('loggedin')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('register')

def loggedin(request):
    logout(request)
    return render(request, 'logincomplete.html')

