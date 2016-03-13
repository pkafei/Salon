from django.conf.urls import include, url
from django.contrib import admin
from . import views

#Wagtail Url Impors
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls


urlpatterns = [
    url(r'^$', views.Landing.as_view(), name='landing'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^services/', views.Services.as_view(), name='services'),
    url(r'blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

   #Wagtail Imports
   url(r'^cms/', include(wagtailadmin_urls)),
   url(r'^documents/', include(wagtaildocs_urls)),
   url(r'^pages/', include(wagtail_urls)),
]
