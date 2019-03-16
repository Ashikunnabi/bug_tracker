from bug_tracker import credentials
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.core.mail import send_mail
import random
from django.shortcuts import render, redirect

from .decorators import has_access


@login_required(login_url='login')
@has_access(allowed_roles=['superuser', 'admin'])
def registration_view(request):
    """ Register new employee only SUPERUSER and ADMIN has the power to add """
    if request.method == "POST":
        employee_id = request.POST['employeeID']             # Collecting employee id
        password    = request.POST['password']               # Collecting password
        # Create user and save to the database
        user = User.objects.create_user(employee_id, 'youremail@yourmail.com', password)
        user.save()
        # Add employee to a 'employee' group
        group = Group.objects.get(name='employee')
        group.user_set.add(user)        
        context = {'success': 'Employee successfully added.'}
        return render(request, 'authentication/registration.html', context)
    else:
        return render(request, 'authentication/registration.html')
        
        
def login_view(request):
    """     Login      """
    if request.method == "POST":                        # If method=POST then request is valid otherwise not
        employee_id = request.POST['employeeID']        # Collecting employee id
        password    = request.POST['password']          # Collecting password
        user = authenticate(username=employee_id, password=password) # If user is valid then authenticte otherwise not
        if user is not None:
            login(request, user)                        # If valid user then login
            return redirect('/')
        else:                                           # If username / password is wrong
            context={"error": "Invalid Employee ID / Password."}
            return render(request, 'authentication/login.html', context)
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'authentication/login.html')
    
    
@login_required(login_url='login')   
@has_access(allowed_roles=['superuser', 'admin', 'employee'])
def logout_view(request):
    """ Logout for all users """
    logout(request)
    return redirect(login_view)    
    
    
def forgot_pass_view(request):
    """ If users forgot password """
    if request.method == "POST":
        employee_id = request.POST['employeeID']       # Collecting employee id
        email       = request.POST['email']            # Collecting email
        try:
            user = User.objects.get(username=employee_id)    # Getting all info of user
            if user.email == email:
                security_code = send_email(email)            # Sending email to the users emal
            else:            
                context = {'error': 'Invalid Credentials'}
                return render(request, 'authentication/forgotPass01.html', context) 
            request.session['SECURITY_CODE'] = security_code
            request.session['EMPLOYEE_ID'] = employee_id
            return render(request, 'authentication/forgotPass02.html')
        except:            
            context = {'error': 'Invalid Credentials'}
            return render(request, 'authentication/forgotPass01.html', context)
    else:
        return render(request, 'authentication/forgotPass01.html')


def send_email(email):
    code = ''
    for x in range(6):
        code += str(random.randint(1,9))
        
    send_mail(
        'Bug Tracker - Forgot Password',
        'Here is the Security Code: '+code+'. Do not share the code. Do not replay.',
        'ashiktuhin12@gmail.com',
        [email],
        fail_silently=False,
    ) 
    return code    

   
def security_code_view(request):
    """ If users forgot password """
    if request.method == "POST":    
        security_code = request.POST['securityCode']       # Collecting security code
        SECURITY_CODE = request.session['SECURITY_CODE']
        if SECURITY_CODE == security_code:
            return render(request, 'authentication/changePassword.html') 
            print(SECURITY_CODE)
        else:
            del request.session['SECURITY_CODE']    # False attemp DELETE session
            del request.session['EMPLOYEE_ID']      # False attemp DELETE session
            context = {'error': 'Invalid Securty Code'}
            return render(request, 'authentication/forgotPass01.html', context)
    else:
        return render(request, 'authentication/login.html')          

   
def change_password_view(request):
    """ If users forgot password """
    if request.method == "POST":    
        password = request.POST['password']       # Collecting password
        EMPLOYEE_ID = request.session['EMPLOYEE_ID']
        user = User.objects.get(username=EMPLOYEE_ID)    # Getting all info of user
        user.set_password(password) 
        user.save()
        context = {'success': 'Successfully Password Changed.'}
        return render(request, 'authentication/login.html', context) 
    else:
        return render(request, 'authentication/login.html')
        
        