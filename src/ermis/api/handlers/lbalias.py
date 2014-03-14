from django.conf import settings
from sys import stderr

from piston.handler import BaseHandler
from piston.utils import validate
#from piston.utils import require_mime

from api.handlers import common



class ListHandler(BaseHandler):
	allowed_methods = ('GET',)

	def read(self, request):
		return common.list_alias(request)


class AddHandler(BaseHandler):
	allowed_methods = ('POST',)

#	@require_mime('json')
	def create(self, request):
		return common.add_alias(request)	


class UpdateHandler(BaseHandler):
	allowed_methods = ('PUT',)

	def update(self, request, name):
		return common.update_alias(request, str(name))		


class DeleteHandler(BaseHandler):
	allowed_methods = ('DELETE',)

	def delete(self, request, name):
		return common.delete_alias(request, str(name))	

