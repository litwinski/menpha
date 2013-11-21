from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',

    # Strictly related to Main app
    url(r'^$', views.intro, name='intro'),

    url(r'^app/$', views.home, name='home'),

    url(r'^app/search/$', views.search, name='search'),

    url(r'^app/add/$', views.create.as_view(), name='add'),
    #url(r'^app/add/$', views.add, name='add'),

    url(r'^app/success/', views.success, name='success'),

    url(r'^app/detail/(?P<slug>\d+)/$', views.detail, name='detail'),

    url(r'^app/edit/(?P<slug>\d+)/$', views.update.as_view(), name='edit'),
    #url(r'^app/edit/(?P<item_imei>\d+)/$', views.edit, name='edit'),

    url(r'^app/edit/$', views.edit_info, name='edit'),

	#delete listing
    url(r'^app/delete/(?P<slug>\d+)/$', views.deleteItem.as_view(), name='delete'),
	#url(r'^app/delete/(?P<item_imei>\d+)/$', views.delete, name='delete'),
	#url(r'^app/deleted/(?P<item_imei>\d+)/', views.deleted, name='deleted'),

    #My Account listings
	url(r'^app/my-list/', views.myList, name='myList'),

    #External links
    #check registration.backends.default.urls for profile link

    #Just for testing
    url(r'^test/', views.base, name='base'),

)
