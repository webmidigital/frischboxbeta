from urllib import request

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from smtplib import SMTP

from django.http import HttpResponse
from frischboxadmin.models import our_cities
from frischboxadmin.models import Post
from frischboxadmin.models import Bulk_orders
from frischboxadmin.models import General_enquiries
from frischboxadmin.models import Policies
from frischboxadmin.models import Packages
from frischboxadmin.models import sliderimages


# Homepage Functions


def index(request):
    post = Post.objects.all()
    slider = sliderimages.objects.all()
    packages = Packages.objects.all()
    return render(request, 'index.html', {'postall': post, 'sliderall': slider, 'packagesall': packages})


def about(request):
    return render(request, 'about.html')

def status(request):
    return render(request, 'status.html')


def policies(request):
    return render(request, 'policies.html')


def policydetails(request, postid):
    policydetails = Policies.objects.get(slug=postid)

    data = {
        'policydetails': policydetails
    }
    return render(request, 'policies.html', data)


# Enquiries
def bulk(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        print(name, email, mobile, message)
        bcontact = Bulk_orders(name=name, email=email, mobile=mobile, message=message)
        bcontact.save()
        return HttpResponse(" <h3> Thanks for Contact, Our Team will be Reply within 24 hrs.</h3>")
    return render(request, 'bulk_order.html')


def contactform(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, mobile, subject, message)
        newenq = General_enquiries(name=name, email=email, mobile=mobile, subject=subject, message=message)
        newenq.save()
        return HttpResponse(" <h3> Thanks for Contact, Our Team will be Reply within 24 hrs.</h3>")
    return render(request, 'contact.html')


# Account Functions

# My Account Functions


# Blog Functions

def blog(request):
    blogs = Post.objects.all()
    return render(request, 'blog.html', {'blogsall': blogs})


def postdetails(request, postid):
    postdetails = Post.objects.get(slug=postid)

    data = {
        'postdetails': postdetails
    }
    return render(request, 'single_post.html', data)


# Products Functions




# Subscription Functions

def subscriptions(request):
    packages = Packages.objects.all()
    return render(request, 'subscriptions.html', {'allpackages': packages})



# Delivery Functions


# Master Functions

def cities(request):
    cities = our_cities.objects.all()
    return render(request, 'cities.html', {'citiesall': cities})


# cart functions


#def checkout_detail(request):
    #outitem = Product.objects.all()
    #return render(request, 'checkout.html', {'outall': outitem})




