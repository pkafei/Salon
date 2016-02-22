from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.Landing.as_view(), name='landing'),
    url(r'^contact/', views.Contact.as_view(), name='contact'),
    url(r'^services/', views.Contact.as_view(), name='service'),
    url(r'blog/', include('blog.urls')),
    #url(r'^$', 'salon_app.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
