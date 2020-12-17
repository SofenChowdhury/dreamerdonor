from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.shortcuts import redirect
import uuid
from .models import UserInfo,Role
from Dreamer.models import Idea,IdeaImage
# Create your views here.


def Index(request):
    title = "User Registration"
    role  = Role

    return render(request, 'frontend/user/index.html',{
        'title':title,
        'Role':role
    })

def register_user(request):
    first_name  = request.POST['email'].split('@')
    email       = request.POST['email']
    password    = request.POST['password1']
    re_password = request.POST['password2']

    user_code   = uuid.uuid4().hex[:6].upper()

    check_user  = User.objects.filter(email= email)

    if check_user:
        messages.warning(request,'UserName or Email Already exist !!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if password != re_password:
        messages.warning(request,'Password Doesn`t match !!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    users = User()

    users.first_name    = first_name[0];
    users.email         = request.POST['email'];
    users.username      = first_name[0];
    users.password      = make_password(request.POST['password1']);
    users.is_staff      = True;

    users.save()

    user_ingo_id = User.objects.order_by('-id').first()

    user_info = UserInfo()

    user_id_id  = user_ingo_id.id;
    # phone       = request.POST['phone'];
    # address     = request.POST['address'];
    # country     = request.POST['country'];
    # role        = request.POST['role'];
    try:
        image     = request.FILES['image'];
        check     = 1
    except MultiValueDictKeyError:
        check     = 0

    if check>0:

        userInfo = UserInfo(user_id_id  = user_id_id,
                        user_code       = user_code,
                        image           = image,
                        role            = 'Dreamer')
        userInfo.save()
        messages.success(request,'Dreamer Registered Successfully !!')
    else:
        userInfo = UserInfo(user_id_id  = user_id_id,
                        user_code       = user_code,
                        role            = 'Dreamer')
        userInfo.save()

    messages.success(request,'Dreamer Registered Successfully !!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_profile(request):

    auth_id = request.POST['auth_id']
    user_id = request.POST['id']

    update_user = User.objects.get(id=auth_id)

    if user_id:
        update_user_info        = UserInfo.objects.get(id=user_id)

        update_user.first_name  = request.POST['first_name']
        update_user.last_name   = request.POST['last_name']
        update_user.email       = request.POST['email']

        update_user.save()

        update_user_info.phone      = request.POST['phone']
        update_user_info.address    = request.POST['address']
        update_user_info.country    = request.POST['country']
        update_user_info.role       = request.POST['role']

        try:

            update_user_info.image = request.FILES['image']
            update_user_info.save()
        except MultiValueDictKeyError:
            update_user_info.save()

        messages.success(request,'User Profile Updated Done  Successfully !!')
    else:

        update_user.first_name  = request.POST['first_name']
        update_user.last_name   = request.POST['last_name']
        update_user.email       = request.POST['email']

        update_user.save()
        phone   = request.POST['phone'];
        address = request.POST['address'];
        country = request.POST['country'];
        image   = request.FILES['image'];
        role    = request.POST['role']

        userInfo = UserInfo(user_id_id   = request.user.id,
                            phone        = phone,
                            address      = address,
                            country      = country,
                            image        = image,
                            role         = role)
        userInfo.save()
        messages.success(request,'User Profile Updated Done  Successfully !!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def Dashboard(request):
    title = " User Profile "
    role  = Role
    if request.user.is_authenticated:
        current_user = request.user

        # user_details = UserInfo.objects.filter(reg_user_id=current_user.id);
        user_details        = UserInfo.objects.filter(user_id_id=request.user.id).first();
        posted_idias        = Idea.objects.filter(user_id=request.user.id).all();
        my_approvals        = Idea.objects.filter(user_id=request.user.id,status='1').all();
        my_pandings         = Idea.objects.filter(user_id=request.user.id,status='0').all();
        my_soldout          = Idea.objects.filter(user_id=request.user.id,status='2').all();

        count_posted_properties = posted_idias.count()
        count_my_approvals      = my_approvals.count()
        count_my_pandings       = my_pandings.count()
        count_my_soldout        = my_soldout.count()

        return render(request, 'frontend/user/dashboard.html', {'title': title,
                                                        'current_user': current_user,
                                                        'user_details': user_details,
                                                        'posted_idias':posted_idias,
                                                        'my_approvals':my_approvals,
                                                        'my_pandings':my_pandings,
                                                        'count_posted_properties':count_posted_properties,
                                                        'count_my_approvals':count_my_approvals,
                                                        'count_my_pandings':count_my_pandings,
                                                        'my_soldout':my_soldout,
                                                        'count_my_soldout':count_my_soldout,
                                                        })
    else:
        return redirect('/')

