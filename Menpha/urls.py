from django.conf.urls import patterns, include, url
from . import views

from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# For Admin Page
    url(r'^admin/', include(admin.site.urls)),

    # intro page
    url(r'^', include('main.urls'), name='intro'),

    # Sitewide Statics
    url(r'^about/$', views.about, name='about'),

    url(r'^contact/', views.contact, name='contact'),

    url(r'^privacy/', views.privacy, name='privacy'),

    url(r'^team/', views.team, name='team'),

    url(r'^learn/', views.learn, name='learn'),

)

urlpatterns += patterns('',

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),

)