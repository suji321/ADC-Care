from django.contrib.auth import login, logout,authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import User
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token

# Create your views here.

def landing(request):
    return render(request, 'landing.html')


def register(request):
    return render(request, 'register.html')


def error(request):
    return render(request, 'error.html')

class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'patregister.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'docregister.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor :
                login(request,user)
                return redirect('home')
            elif user is not None and user.is_patient :
                login(request,user)
                return redirect('phome')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('login')

def loggedin(request):
    logout(request)
    return render(request, 'logincomplete.html')

def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name':'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token':default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                   
                    return redirect('password_reset_done')
    password_reset_form = PasswordResetForm()
    return render(request, 'password/password_reset.html', {'password_reset_form':password_reset_form})

def activate(request, uidb64, token):  
 
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('login')
    else:  
        return HttpResponse('Activation link is invalid!')  

def error_404(request, exception):
        data = {}
        return render(request,'error.html', data)