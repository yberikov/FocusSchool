from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from focus.forms import UserForm, UserProfileInfoForm, FocusPlan1Form, FocusTeach1Form, FocusEvaluation1Form, \
    FocusComplex1Form, PdgForm
from focus.models import UserProfileInfo, FocusPlan1, FocusTeach1, FocusEvaluation1, FocusComplex1


def index(request):
    current_user = None
    if request.user.is_authenticated:
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)

    return render(request, 'focus/index.html', {'current_user': current_user})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Неправильный логин или пароль')
            return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request, 'focus/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('user_login'))

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'focus/registration.html', {'user_form': user_form,
                                                       'profile_form': profile_form,
                                                       'registered': registered})


def userinfo(request):
    user_info = 'Friend'
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST, instance=request.user)
        profile_form = UserProfileInfoForm(data=request.POST, instance=request.user)

        # if user_form.is_valid() and profile_form.is_valid():
        user_info.username = user_form['username'].value()
        user_info.email = user_form['email'].value()
        user_info.first_name = user_form['first_name'].value()
        user_info.last_name = user_form['last_name'].value()
        current_user.user_middlename = profile_form['user_middlename'].value()
        user_info.save()
        current_user.save()
        registered = True
        return HttpResponseRedirect(reverse('userinfo'))

        # else:
        #    print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'focus/userinfo.html', {'user_form': user_form,
                                                   'profile_form': profile_form,
                                                   'registered': registered,
                                                   'user_info': user_info, 'current_user': current_user})


def add_pdg(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)

    if request.method == 'POST':

        pdg_form = PdgForm(data=request.POST)

        if pdg_form.is_valid():
            record = pdg_form.save(commit=False)

            record.user = current_user
            record.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(pdg_form.errors)

    else:
        pdg_form = PdgForm()
    return render(request, 'focus/add_pdg.html', {'pdg_form': pdg_form,
                                                  'title': 'Создание отчета', 'current_user': current_user,
                                                  })


def focusplan1(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
        user_list = UserProfileInfo.objects.all().exclude(
            user_id=current_user.id)

    if request.method == 'POST':
        focusplan1_form = FocusPlan1Form(data=request.POST)

        if focusplan1_form.is_valid():
            record = focusplan1_form.save(commit=False)
            current_userprofileinfo = UserProfileInfo.objects.get(user_id=user_info.id)
            record.user_observer = current_userprofileinfo
            record.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(focusplan1_form.errors)
    else:
        focusplan1_form = FocusPlan1Form()
    return render(request, 'focus/focusplan1.html', {'focusplan1_form': focusplan1_form,
                                                     'title': 'Создание отчета', 'current_user': current_user,
                                                     'user_list': user_list})


def focusteach1(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
        user_list = UserProfileInfo.objects.all().exclude(
            user_id=current_user.id)

    if request.method == 'POST':
        focusteach1_form = FocusTeach1Form(data=request.POST)

        if focusteach1_form.is_valid():
            record = focusteach1_form.save(commit=False)

            current_userprofileinfo = UserProfileInfo.objects.get(user_id=user_info.id)
            record.user_observer = current_userprofileinfo
            record.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            print(focusteach1_form.errors)

    else:
        focusteach1_form = FocusTeach1Form()
    return render(request, 'focus/focusteach1.html', {'focusteach1_form': focusteach1_form,
                                                      'title': 'Создание отчета', 'current_user': current_user,
                                                      'user_list': user_list})


def focusevaluation1(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
        user_list = UserProfileInfo.objects.all().exclude(
            user_id=current_user.id)
    if request.method == 'POST':
        focusevaluation1_form = FocusEvaluation1Form(data=request.POST)

        if focusevaluation1_form.is_valid():
            record = focusevaluation1_form.save(commit=False)

            current_userprofileinfo = UserProfileInfo.objects.get(user_id=user_info.id)
            record.user_observer = current_userprofileinfo
            record.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            print(focusevaluation1_form.errors)

    else:
        focusevaluation1_form = FocusEvaluation1Form()
    return render(request, 'focus/focusevaluation1.html', {'focusevaluation1_form': focusevaluation1_form,
                                                           'title': 'Создание отчета', 'current_user': current_user,
                                                           'user_list': user_list})


def focuscomplex1(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
        user_list = UserProfileInfo.objects.all().exclude(
            user_id=current_user.id)
    if request.method == 'POST':
        focuscomplex1_form = FocusComplex1Form(data=request.POST)

        if focuscomplex1_form.is_valid():
            record = focuscomplex1_form.save(commit=False)

            current_userprofileinfo = UserProfileInfo.objects.get(user_id=user_info.id)
            record.user_observer = current_userprofileinfo
            record.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            print(focuscomplex1_form.errors)

    else:
        focuscomplex1_form = FocusComplex1Form()
    return render(request, 'focus/focuscomplex1.html', {'focuscomplex1_form': focuscomplex1_form,
                                                        'title': 'Создание отчета', 'current_user': current_user,
                                                        'user_list': user_list})


def teacher_evaluation(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
        focusplan1_records = FocusPlan1.objects.all().filter(user_teacher_id=user_info.id)
        focusteach1_records = FocusTeach1.objects.all().filter(user_teacher_id=user_info.id)
        focusevaluation1_records = FocusEvaluation1.objects.all().filter(user_teacher_id=user_info.id)
        focuscomplex1_records = FocusComplex1.objects.all().filter(user_teacher_id=user_info.id)

    return render(request, 'focus/teacher.html',
                  {'focusplan1_records': focusplan1_records, 'focusteach1_records': focusteach1_records,
                   'focusevaluation1_records': focusevaluation1_records, 'focuscomplex1_records': focuscomplex1_records,
                   'current_user': current_user})


def observer_evaluation(request):
    current_user = None
    if request.user.is_authenticated:
        user_info = request.user
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
        focusplan1_records = FocusPlan1.objects.all().filter(user_observer_id=user_info.id)
        focusteach1_records = FocusTeach1.objects.all().filter(user_observer_id=user_info.id)
        focusevaluation1_records = FocusEvaluation1.objects.all().filter(user_observer_id=user_info.id)
        focuscomplex1_records = FocusComplex1.objects.all().filter(user_observer_id=user_info.id)

    return render(request, 'focus/observer.html',
                  {'focusplan1_records': focusplan1_records, 'focusteach1_records': focusteach1_records,
                   'focusevaluation1_records': focusevaluation1_records, 'focuscomplex1_records': focuscomplex1_records,
                   'current_user': current_user})


def report_details(request, id):
    current_user = None
    if request.user.is_authenticated:
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
    report = FocusPlan1.objects.get(id=id)

    if request.method == 'POST':
        focusplan1_form = FocusPlan1Form(data=request.POST, instance=report)

        if focusplan1_form.is_valid():
            report.subject = focusplan1_form.cleaned_data['subject']

            report.save()

            return HttpResponseRedirect(reverse('index'))

        else:
            print(2222)
            print(focusplan1_form.errors)

    else:
        focusplan1_form = FocusPlan1Form()
    return render(request, 'focus/focusplan1.html', {'focusplan1_form': focusplan1_form,
                                                     'title': 'Редактирование отчета', 'current_user': current_user})


def admin_panel(request):
    current_user = None
    if request.user.is_authenticated:
        current_user = UserProfileInfo.objects.get(user_id=request.user.id)
    search_post = request.GET.get('search')
    posts1 = FocusPlan1.objects.all()
    posts2 = FocusTeach1.objects.all()
    posts3 = FocusEvaluation1.objects.all()
    posts4 = FocusComplex1.objects.all()
    if search_post:
        users = User.objects.all().filter(last_name__contains=search_post)
        for i in users:
            posts1 = FocusPlan1.objects.all().filter(user_teacher=i.id)

            posts2 = FocusTeach1.objects.all().filter(user_teacher=i.id)
            posts3 = FocusEvaluation1.objects.all().filter(user_teacher=i.id)
            posts4 = FocusComplex1.objects.all().filter(user_teacher=i.id)

    return render(request, 'focus/admin_panel.html',
                  {'posts1': posts1, 'posts2': posts2, 'posts3': posts3, 'posts4': posts4,
                   'current_user': current_user})
