from django.conf.urls import patterns, include, url

from piston.resource import Resource
from api.handlers import lbalias


urlpatterns = patterns('',
	url(r'^api/lbalias/list$',Resource(lbalias.ListHandler)),
	url(r'^api/lbalias/add$',Resource(lbalias.AddHandler)),
	url(r'^api/lbalias/update/(?P<name>.*)$',Resource(lbalias.UpdateHandler)),
	url(r'^api/lbalias/delete/(?P<name>.*)$',Resource(lbalias.DeleteHandler)),	
)
