from django.shortcuts import render


# Create your views here.



def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
   return render(request, 'website/contact.html')

def education_view(request):
   return render(request, 'website/education.html')

def experience_view(request):
   return render(request, 'website/experience.html')

def single_view(request):
   return render(request, 'website/single.html')

def skills_view(request):
   return render(request, 'website/skills.html')

def certificates_view(request):
   return render(request, 'website/certificates.html')