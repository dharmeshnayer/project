from django.conf.urls import patterns, include, url
from propertyapp import views
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'propertylist.views.home', name='home'),
    # url(r'^propertylist/', include('propertylist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^addproperty/',views.createproperty),
    url(r'^logout/',views.index),
    url(r'^editproperty/$',views.editproperty,name="editproperty"),
    url(r'^deleteproperty/$',views.deleteproperty),
    url(r'^signup/$', views.signup),
)