from django.shortcuts import render,  get_object_or_404
from website.models import Certificates,Institution
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from website.forms import  contactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.



def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
   if request.method == 'POST':
      form = contactForm(request.POST)
      if form.is_valid():
         form.instance.name = 'anonymous'
         form.save()
         messages.add_message(request, messages.SUCCESS, 'we got your ticket')
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      else:
         messages.add_message(request, messages.ERROR, 'something went wrong')
   form = contactForm()        
   return render(request, 'website/contact.html', {'form':form})

def education_view(request):
   return render(request, 'website/education.html')

def experience_view(request):
   return render(request, 'website/experience.html')

def skills_view(request):
   return render(request, 'website/skills.html')

def certificates_view(request, **kwargs):
   certificates = Certificates.objects.all()    
   if kwargs.get('inst_name') != None:
      certificates = certificates.filter(institution__name=kwargs['inst_name'])
      
   
  
   context = {'certificates': certificates}
   return render(request, 'website/certificates.html', context)

def single_view(request, pid):
   certificates = Certificates.objects.all()
   certificate = get_object_or_404(certificates,pk=pid)
   context = {'certificate': certificate}
   
   return render(request, 'website/single.html', context)

def newsletter_view(request):
   if request.method == 'POST':
      form = NewsletterForm(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, 'We got your email')
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      else:
        messages.add_message(request, messages.ERROR, 'Something went wrong') 