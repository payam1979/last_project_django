from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from website.models import Certificates

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    
    def items(self):
        return ['website:index', 'website:about', 'website:contact','website:certificates', 'website:education', 'website:experience', 'website:skills',  ]
    
    def location(self, item):
        return reverse(item)
    
    
    
class WebsiteSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    
    def items(self):
        return Certificates.objects.all()
    
    def lastmod(self, obj):
        return obj.issu_date
    
    def location(self, item):
        return reverse("website:single", kwargs={'pid': item.id})