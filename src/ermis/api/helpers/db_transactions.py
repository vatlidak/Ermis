import logging

from aliases.models import Alias

def RetrieveAll():
	try:
		response = Alias.objects.values('alias_name','type')
	except Exception as detail:
		raise Exception(detail)
	return response

def RegisterAlias(params):
	try:
		new_alias = Alias(alias_name=params['alias_name'], type=params['type'])
 		new_alias.save()
	except Exception as detail:
  		raise Exception(detail)
		

def RemoveAlias(params):
	try:
		deprecated_alias = Alias.objects.get(alias_name=params['alias_name'])
 		deprecated_alias.delete()
	except Exception as detail:
		raise Exception(detail)

def ModifyAlias(params):
	try:
		deprecated_alias = Alias.objects.get(alias_name=params['alias_name'])
		deprecated_alias.type = params['type']
		deprecated_alias.save()
	except Exception as detail:
		raise Exception(detail)
