from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Dreamer.models import Idea as DreamerIdea,IdeaImage
from Master.models import AboutUs,TermsCondition,Companyinfo
from UserInfo.models import UserInfo,Role
# Create your views here.
def home(request):
    companyInfo  = Companyinfo.objects.first()
    get_idea     = DreamerIdea.objects.filter(status=1).order_by('-id')[:8].all()
    get_dreamer  = UserInfo.objects.filter(role = 'Dreamer').exclude(image='').order_by('-id')[:4].all()
    get_donor    = UserInfo.objects.filter(role = 'Donor').exclude(image='').order_by('-id')[:4].all()

    get_all_dreamers = UserInfo.objects.filter(role = 'Dreamer').filter(image__isnull=False).order_by('-id')[:15].all()
    return render(request, 'frontend/home.html',{
        'get_idea':get_idea,
        'get_dreamer':get_dreamer,
        'get_donor':get_donor,
        'get_all_dreamers':get_all_dreamers,
        'companyInfo':companyInfo,
        })

def idea_list(request):
    get_idea            = DreamerIdea.objects.filter(status=1).order_by('-id').all()
    get_latest_idea     = DreamerIdea.objects.filter(status=1).order_by('-id')[:4].all()

    return render(request, 'frontend/dreamer/idea_list.html',{
        'get_idea':get_idea,
        'get_latest_idea':get_latest_idea
        })

def SearchIdea(request,id):
    get_idea            = DreamerIdea.objects.filter(status=1).filter(user_id_id=id).order_by('-id').all()
    get_latest_idea     = DreamerIdea.objects.filter(status=1).order_by('-id')[:4].all()

    return render(request, 'frontend/dreamer/search_by_user.html',{
        'get_idea':get_idea,
        'get_latest_idea':get_latest_idea
        })

def idea_details(request,id):
    title = "Idea Details"
    get_idea        = DreamerIdea.objects.filter(id=id).exclude(status=0).first()
    idea_image      = IdeaImage.objects.filter(idea_id_id=id).order_by('-id').all()
    active_image    = IdeaImage.objects.filter(idea_id_id=id).first()
    get_latest_idea = DreamerIdea.objects.exclude(status='0').order_by('-id')[:4].all()
    paginator       = Paginator(get_idea,10)

    current_user    = request.user
    user_details    = UserInfo.objects.filter(user_id_id=get_idea.user_id_id).first()


    # try:
    #     page = int(request.GET.get('page','1'))
    # except:
    #     page = 1
    # try:
    #     posts = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     posts = paginator.page(paginator.num_pages)

    return render(request, 'frontend/dreamer/idea_details.html',{
        'title':title,
        'get_idea':get_idea,
        'get_latest_idea':get_latest_idea,
        'idea_image':idea_image,
        'active_image':active_image,
        'paginator':paginator,
        'current_user':current_user,
        'user_details':user_details
        })

def contact(request):
    title = "Contact"
    current_user    = request.user
    return render(request, 'frontend/contact.html',{
        'title':title,
        'current_user':current_user,
        })
def faqs(request):
    title = "FAQs"
    current_user    = request.user
    return render(request, 'frontend/faqs.html',{
        'title':title,
        'current_user':current_user,
        })
def about(request):
    title = "About Us"
    about_us        = AboutUs.objects.first()
    return render(request, 'frontend/about.html',{
        'title':title,
        'about_us':about_us,
        })

def terms_and_conditions(request):
    title = "Terms and conditions"
    terms_condition        = TermsCondition.objects.all()
    return render(request, 'frontend/terms_and_conditions.html',{
        'title':title,
        'terms_condition':terms_condition,
        })

def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user     = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.info(request, 'Username OR password is incorrect')
    return redirect('home')

def all_locations(request):
    get_location = UserInfo.objects.values('country').all().distinct()
    data         = list(get_location)

    return JsonResponse(data, safe=False )

# ***************** Search **********************
def search(request):
    title   = "Dreamer & Donor"
    donor   = request.GET.get('donor')
    dreamer = request.GET.get('dreamer')
    get_latest_idea     = DreamerIdea.objects.filter(status=1).order_by('-id')[:4].all()
    if donor and dreamer:
        getUsers  = UserInfo.objects.filter(role__contains = 'Dreamer').filter(country = dreamer)|UserInfo.objects.filter(role__contains='Donor').filter(country = donor).order_by('-id').all()
    elif dreamer:
        getUsers  = UserInfo.objects.filter(role = 'Dreamer').filter(country = dreamer).order_by('-id').all()
    else:
        getUsers  = UserInfo.objects.filter(role = 'Donor').filter(country = donor).order_by('-id').all()
    return render(request, 'frontend/dreamer/search_user.html',{
        'title':title,
        'getUsers':getUsers,
        'get_latest_idea':get_latest_idea,
        })

def search_idea(request):
    title           = "Dreamer & Donor"
    search_title    = request.GET.get('search_title')
    get_idea            = DreamerIdea.objects.filter(title__icontains=search_title).exclude(status='0').order_by('-id').all()
    get_latest_idea     = DreamerIdea.objects.filter(status=1).order_by('-id')[:4].all()

    return render(request, 'frontend/dreamer/search_idea.html',{
        'title':title,
        'get_idea':get_idea,
        'get_latest_idea':get_latest_idea,
        })
