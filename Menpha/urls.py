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
    url(r'^about-menpha/$', views.about, name='about'),

    url(r'^contact-menpha/', views.contact, name='contact'),

    url(r'^privacy-terms/', views.privacy, name='privacy'),

    url(r'^team-menpha/', views.team, name='team'),

    url(r'^learn-menpha/', views.start, name='start'),

    url(r'^story-behind/', views.story, name='story'),

    url(r'^faq/', views.faq, name='faq'),

    url(r'^donate/', views.donate, name='donate'),

    url(r'^technology/', views.technology, name='technology'),

    url(r'^developer/', views.developer, name='developer'),
)

urlpatterns += patterns('',

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),

)