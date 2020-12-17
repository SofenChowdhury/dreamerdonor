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
from .models import Idea,IdeaImage
from Master.models import Master

# Create your views here.
@login_required(login_url='/admin/login/')
def PostIdea(request):
    companyinfo = Master.objects.first()
    return render(request, 'frontend/dreamer/idea.html',{
        'companyinfo':companyinfo
        })

def SubmitIdea(request):
    title       = request.POST['title']
    sub_title   = request.POST['sub_title']
    description = request.POST['description']
    video_link  = request.POST['video_link']
    user_id     = request.user.id
    images      = request.FILES.getlist('images')

    # return HttpResponse(request.FILES.getlist('video'))
    if (request.FILES.getlist('video')):
        video       = request.FILES['video']

        SaveIdea = Idea(title   = title,
                sub_title       = sub_title,
                video_link      = video_link,
                video           = video,
                status          = 0,
                user_id         = User(user_id),
                description     = description)
    else:
        SaveIdea = Idea(title   = title,
                sub_title       = sub_title,
                video_link      = video_link,
                status          = 0,
                user_id         = User(user_id),
                description     = description)

    SaveIdea.save()

    if images:
        for image in images:
            saveIdea_image = IdeaImage(idea_id=Idea(SaveIdea.id), Image=image)
            saveIdea_image.save()

    messages.success(request,'Idea Posted Successfully !!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def ChangeStatus(request,id1,id2):
    up_status = Idea.objects.filter(id=id2).update(status=id1)
    return HttpResponse(id1);
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def IdeaDelete(request,id):

    del_Idea = Idea.objects.filter(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
