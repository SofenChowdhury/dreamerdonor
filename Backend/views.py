from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.safestring import SafeData, SafeString, mark_safe
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator
import datetime
from Dreamer.models import Idea as DreamerIdea,IdeaImage
from UserInfo.models import UserInfo,Role

# Create your views here.
@login_required(login_url='/admin/login/')
def adminDashboard(request):
    title = "Admin Dashboard"

    return render(request,'admin/dashboard.html',{
        'title':title,
        })
@login_required(login_url='/admin/login/')
def Idea(request):
    title = "Idea List"

    current_user = request.user
    get_userinfo = UserInfo.objects.filter(user_id_id=request.user.id).first()

    get_idea     = DreamerIdea.objects.order_by('-id').all()
    # followup     = current_user.has_perm('followup.add_followup')
    # permissions = Permission.objects.filter(user=request.user,name='Can view property').first()

    return render(request,'admin/dreamer/idea.html',{
        'title':title,
        'current_user':current_user,
        'get_userinfo':get_userinfo,
        'get_idea':get_idea,
        })
def IdeaEdit(request,id):
    title = "Idea"

    current_user    = request.user
    get_userinfo    = UserInfo.objects.filter(user_id_id=request.user.id).first()
    get_images      = IdeaImage.objects.filter(idea_id=id).all()
    get_idea        = DreamerIdea.objects.filter(id=id).first()
    # followup     = current_user.has_perm('followup.add_followup')
    # permissions = Permission.objects.filter(user=request.user,name='Can view property').first()

    return render(request,'admin/dreamer/edit.html',{
        'title':title,
        'current_user':current_user,
        'get_userinfo':get_userinfo,
        'get_idea':get_idea,
        'get_images':get_images,
        })

def updateIdea(request):
    images              = request.FILES.getlist('images')
    id                  = request.POST['id']

    update_idea         = DreamerIdea.objects.get(id=request.POST['id'])
    update_image        = IdeaImage.objects.filter(idea_id=request.POST['id'])

    if images:
        update_image.delete()

    update_idea.title           = request.POST['title']
    update_idea.sub_title       = request.POST['sub_title']
    update_idea.description     = request.POST['description']
    update_idea.video_link      = request.POST['video_link']
    if request.FILES.get('plan_doc'):
        update_idea.plan_doc    = request.FILES['plan_doc']
    try:
        update_idea.video   = request.FILES['video']
        update_idea.save()
    except MultiValueDictKeyError:
        update_idea.save()

    for image in images:
        proprty_image = IdeaImage(idea_id=DreamerIdea(id), Image=image)
        proprty_image.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def IdeaImages(request,id):

    get_images = IdeaImage.objects.values('Image').filter(idea_id=id).all()
    data = list(get_images)

    return JsonResponse(data, safe=False )

def DeleteIdeaImages(request,id):

    de_idea_image = IdeaImage.objects.filter(id=id).delete()

    return HttpResponse(id)
# *********** User **********************
def GetUser(request):
    title       = "User"
    get_user    = UserInfo.objects.order_by('-id').all()
    return render(request,'admin/user/index.html',{
        'title':title,
        'get_user':get_user,
        })
def UserEdit(request,id):
    title = "User"

    current_user    = request.user
    get_userinfo    = UserInfo.objects.filter(id=id).first()
    role            = Role
    # followup     = current_user.has_perm('followup.add_followup')
    # permissions = Permission.objects.filter(user=request.user,name='Can view property').first()

    return render(request,'admin/user/edit.html',{
        'title':title,
        'get_userinfo':get_userinfo,
        'role':role,
        })

def updateUser(request):

    user_id = request.POST['id']

    update_user = User.objects.get(id=user_id)

    if user_id:
        update_user_info        = UserInfo.objects.get(user_id_id=user_id)

        update_user.username    = request.POST['name']
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

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
