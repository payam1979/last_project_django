from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    
   
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('education', education_view, name='education'),
    path('experience', experience_view, name='experience'),
    path('single/<int:pid>', single_view, name='single'),
    path('skills', skills_view, name='skills'),
    path('certificates', certificates_view, name='certificates'),
    path('certificates/<str:inst_name>', certificates_view, name='certificatesinst'),
    path('newsletter', newsletter_view, name='newsletter'),
    
]
