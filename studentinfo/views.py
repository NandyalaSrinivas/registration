from . models import Registration, Student, Documents
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="//login/")
def index(request):
    student = Registration.objects.all()
    return render(request, 'sudents/home.html', {"index":student})


@login_required(login_url='/login/')
def create_registration(request):
    if request.method == 'GET':
        return render(request, 'sudents/create.html')
    elif request.method == 'POST':
        print request.POST
        print request.FILES
        with transaction.atomic():
            reg = Registration(first_name=request.POST.get('first_name'),
                               last_name=request.POST.get('last_name'),
                               email_id=request.POST.get('email_id')
                               )
            reg.save()
            print request.POST
            stu = Student.objects.create(registration_id=reg.id,
                          date_of_birth=request.POST.get('date_of_birth'),
                          mobile_no=request.POST.get('mobile_no'),
                          address=request.POST.get('address'),
                          roll_no=request.POST.get('roll_no'),
                          d_join_date=request.POST.get('d_join_date')
                          )
            stu.save()
            Documents.objects.create(student_id=stu.id,
                                     ssc=request.FILES['ssc'],
                                     inter=request.FILES['inter'],
                                     degree=request.FILES['degree'],
                                     mca=request.FILES['mca']

                                     )
        return HttpResponseRedirect(reverse('studentinfo:index'))

@login_required(login_url='/login/')
def student_detail(request, registration_id):
    reg = get_object_or_404(Registration, pk=registration_id)
    return render(request, 'sudents/studentdetail.html', {'registration': reg})

def user_regisration(request):
    if request.method == 'GET':
        return render(request, 'sudents/success.html')
    elif request.method == 'POST':
        print request.POST
        #import pdb;pdb.set_trace()
        user_reg= User.objects.create_user(username=request.POST.get('username'),
                                          email=request.POST.get('email'),
                                           password=request.POST.get('password'))
        # user_reg.save()
        #user_reg.set_password(request.POST.get('password'))
        return HttpResponseRedirect(reverse('studentinfo:index'))


def user_login(request):
    # import pdb;pdb.set_trace()debug point
    if request.method == "GET":
        return render(request, "sudents/login.html")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print user
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('studentinfo:index'))
        else:
            return render(request,"sudents/login.html",{"message":"failed"})


def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return render(request, "sudents/logout.html")

