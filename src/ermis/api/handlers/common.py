import logging
import httplib

from django.http import HttpResponse
from django.conf import settings

from piston.handler import BaseHandler
from piston.utils import rc

from api.helpers.db_transactions import RetrieveAll, RegisterAlias, RemoveAlias, ModifyAlias
from api.errors import MalformedParamsError 
 
logger = logging.getLogger(__name__)


def list_alias(request):
	"""
	Function invoked when a GET request is received by the server.
	It returns information about the specified lb alias.
	"""
	try:
		response = RetrieveAll()
		logging.info("Respond to a REST %s request from host %s." % (request.META['REQUEST_METHOD'], request.META['REMOTE_ADDR']))
	except Exception as detail:
		response = rc.BAD_REQUEST
		logging.info("Host %s send me a request causing me trouble. Error: %s" % (request.META['REMOTE_ADDR'],detail))	
		response.write("\n%s\n" % detail)
	return response


def add_alias(request):
	"""
	Function invoked when a POST request is received by the server.
    It adds the specified lb alias in the DB.
	"""
	try:
		type=__validate_type(request)
		params = { "alias_name": request.data['alias_name'],
			"type": type
		}
		RegisterAlias(params)
		response = rc.CREATED
	 	logging.info("Register alias %s with type %s." % (params['alias_name'],params['type']))	
		logging.info("Respond to a REST %s request from host %s." % (request.META['REQUEST_METHOD'], request.META['REMOTE_ADDR']))
	except Exception as detail:
		response = rc.BAD_REQUEST
		logging.info("Host  %s send me a request causing me trouble. Error: %s" % (request.META['REMOTE_ADDR'],detail))
		response.write("\n-%s-\n" % detail)
	return response


def delete_alias(request,name):
	"""
	Function invoked when a DELETE request is received by the server.
	It deletes the specified lb alias from the DB.
	"""
	try:
		params = { "alias_name": name }
		RemoveAlias(params)
		response = rc.DELETED
		logging.info("Delete alias %s." % name)	
		logging.info("Respond to a REST %s request from host %s." % (request.META['REQUEST_METHOD'], request.META['REMOTE_ADDR']))
	except Exception as detail:
		response = rc.BAD_REQUEST
		logging.info("Host  %s send me a request causing me trouble. Error: %s." % (request.META['REMOTE_ADDR'],detail))
		response.write("\n%s\n" % detail)
	return response 


def update_alias(request,name):
	try:
		type=__validate_type(request)
		params = { "alias_name": name,
			"type": type
		}
		ModifyAlias(params)
		response = rc.ALL_OK
		logging.info("Update alias %s." % name)
		logging.info("Respond to a REST %s request " % (request.META['REQUEST_METHOD']))
	except Exception as detail:
		response = rc.BAD_REQUEST
		logging.info("Host  %s send me a request causing me trouble. Error:  %s" % (request.META['REMOTE_ADDR'],detail))
		response.write("\n%s\n" % detail)
	return response 


def __validate_type(request):
	if 'type' not in request.data.keys():
		raise MalformedParamsError("Dictionary key \"type\" not provided. Supported types: external/internal.")
	if 	request.data['type'] not in ["internal", "external"]:
		raise MalformedParamsError("Invalid alias type %s. Supported types: external/internal." % request.data['type'] )
	return request.data['type']
