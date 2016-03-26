from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Landing.as_view(), name='landing'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^services/', views.Services.as_view(), name='services'),
    url(r'blog/', include('blog.urls')),
    #url(r'^$', 'salon_app.views.home', name='home'),
    #url(r'^blog/', include('blog.urlrls')),

	# url(r'^$', views.post_list, name='post_list'),
 #    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
]
