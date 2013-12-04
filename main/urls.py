from django.conf.urls import patterns, include, url

from . import views

from django.conf.urls.static import static
from Menpha import settings

urlpatterns = patterns('',

    # Strictly related to Main app
    url(r'^$', views.intro, name='intro'),

    url(r'^app/$', views.home, name='home'),

    url(r'^app/search/$', views.search, name='search'),

    url(r'^app/add/$', views.Create.as_view(), name='add'),
    #url(r'^app/add/$', views.add, name='add'),

    #url(r'^app/success/', views.success, name='success'),

    url(r'^app/detail/(?P<slug>\d+)/$', views.detail, name='detail'),

    url(r'^app/edit/(?P<slug>\d+)/$', views.Update.as_view(), name='edit'),
    #url(r'^app/edit/(?P<item_imei>\d+)/$', views.edit, name='edit'),

    #url(r'^app/edit/$', views.edit_info, name='edit'),

	#delete listing
    url(r'^app/delete/(?P<slug>\d+)/$', views.DeleteItem.as_view(), name='delete'),
	#url(r'^app/delete/(?P<item_imei>\d+)/$', views.delete, name='delete'),
	#url(r'^app/deleted/(?P<item_imei>\d+)/', views.deleted, name='deleted'),

    #My Account listings
	url(r'^app/my-list/', views.MyList.as_view(), name='myList'),

    #External links
    #check registration.backends.default.urls for profile link

    #Just for testing new additions or features
    url(r'^test/', views.base, name='base'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
