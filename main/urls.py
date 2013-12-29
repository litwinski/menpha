# Urls.py Handwritten by google.com/+Nkansahrexford
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from Menpha import settings

urlpatterns = patterns('',
    # See Menpha.urls for other URLs
    url(r'^$', views.intro_page, name='intro'),

    url(r'^app/$', views.app_home, name='home'),

    url(r'^app/search/$', views.search, name='search'),

    url(r'^app/add/$', views.CreateImei.as_view(), name='add'),

    url(r'^app/detail/(?P<slug>\d+)/$', views.imei_detail, name='detail'),

    url(r'^app/edit/(?P<slug>\d+)/$', views.UpdateImei.as_view(), name='edit'),

    url(r'^app/notify/(?P<slug>\d+)/$', views.notify, name='notify'),

    url(r'^app/notify/thanks/$', login_required(TemplateView.as_view(template_name='notify-thanks.html')),),
    url(r'^app/email/thanks/$', login_required(TemplateView.as_view(template_name='email-thanks.html')),),
	
    url(r'^app/delete/(?P<slug>\d+)/$', views.DeleteImei.as_view(), name='delete'),

	url(r'^app/my-list/', views.ListImei.as_view(), name='myList'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
