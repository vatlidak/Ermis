import httplib
import json

from django.test import TestCase

class ListHandlerTest(TestCase):
	def setUp(self):
		pass

	def test_list_of_aliases(self):	
 		response = self.client.get('/api/lbalias/list')
		self.assertEqual(response.status_code, httplib.OK)		

class AddHandlerTest(TestCase):
	def setUp(self):
		self.good_body_raw = {}
		self.good_body_raw["type"] = "external"
		self.good_body_raw["alias_name"] = "this_is_a_test_alias-1"
		self.good_body = json.dumps(self.good_body_raw)
		self.bad_body_invalid_dict_key_raw={}
		self.bad_body_invalid_dict_key_raw["tyyyyyyyype"] = "external"
		self.bad_body_invalid_dict_key_raw["alias_name"] = "this_is_a_test_alias-1"
		self.bad_body_invalid_dict_key = json.dumps(self.bad_body_invalid_dict_key_raw)
		self.bad_body_invalid_type_raw={}
		self.bad_body_invalid_type_raw["type"] = "exteeeeeeeernal"
		self.bad_body_invalid_type_raw["alias_name"] = "this_is_a_test_alias-1"
		self.bad_body_invalid_type = json.dumps(self.bad_body_invalid_type_raw)

	

	def test_registration_of_alias_good_post_request(self):
		data = self.good_body
		response = self.client.post('/api/lbalias/add', data,
        	content_type='application/json')
		self.assertEqual(response.status_code, httplib.CREATED)


	def test_registration_of_alias_invalid_dict_key(self):
		data = self.bad_body_invalid_dict_key
		response = self.client.post('/api/lbalias/add', data, content_type='application/json')
		self.assertEqual(response.status_code, httplib.BAD_REQUEST)

	def test_registration_of_alias_invalid_type(self):
		data = self.bad_body_invalid_type
		response = self.client.post('/api/lbalias/add', data,
        	content_type='application/json')
		self.assertEqual(response.status_code, httplib.BAD_REQUEST)

	def test_registration_of_existing_alias(self):
		data = self.good_body
		response = self.client.post('/api/lbalias/add', data,
			content_type='application/json')
		self.assertEqual(response.status_code, httplib.CREATED)
		response = self.client.post('/api/lbalias/add', data,
			content_type='application/json')
		self.assertEqual(response.status_code, httplib.BAD_REQUEST)
		
	
class UpdateHandlerTest(TestCase):
	def setUp(self):
		self.good_body_raw = {}
		self.good_body_raw["alias_name"] = "this_is_a_test_alias-1"
		self.good_body_raw["type"] = "internal"
		self.good_body = json.dumps(self.good_body_raw)
		self.bad_body_invalid_dict_key_raw={}
		self.bad_body_invalid_dict_key_raw["tyyyyyyyype"] = "external"
		self.bad_body_invalid_dict_key = json.dumps(self.bad_body_invalid_dict_key_raw)
		self.bad_body_invalid_type_raw={}
		self.bad_body_invalid_type_raw["type"] = "exteeeeeeeeeeeeernal"
		self.bad_body_invalid_type = json.dumps(self.bad_body_invalid_type_raw)

	def test_update_alias_valid(self):
		data = self.good_body
		response = self.client.post('/api/lbalias/add', data, content_type='application/json')
		self.assertEqual(response.status_code, httplib.CREATED)
		response = self.client.put('/api/lbalias/update/this_is_a_test_alias-1', data, 
			content_type='application/json')		
		self.assertEqual(response.status_code, httplib.OK)
	
	def test_update_alias_invalid_dict(self):
		data = self.good_body
		response = self.client.post('/api/lbalias/add', data, content_type='application/json')
		self.assertEqual(response.status_code, httplib.CREATED)
		data = self.bad_body_invalid_dict_key
		response = self.client.put('/api/lbalias/update/this_is_a_test_alias-1', data, 
			content_type='application/json')		
		self.assertEqual(response.status_code, httplib.BAD_REQUEST)
		
	def test_update_alias_invalid_type(self):
		data = self.good_body
		response = self.client.post('/api/lbalias/add', data, content_type='application/json')
		self.assertEqual(response.status_code, httplib.CREATED)
		data = self.bad_body_invalid_type
		response = self.client.put('/api/lbalias/update/this_is_a_test_alias-1', data, 
			content_type='application/json')		
		self.assertEqual(response.status_code, httplib.BAD_REQUEST)

	def test_update_non_existing_alias(self):
		data = self.good_body
		response = self.client.put('/api/lbalias/update/this_alias_never_existed', data,
			content_type='application/json')
		self.assertEqual(response.status_code, httplib.BAD_REQUEST)


class DeleteHandlerTest(TestCase):
	def setUp(self):
		self.good_body_raw = {}
		self.good_body_raw["alias_name"] = "this_is_a_test_alias-1"
		self.good_body_raw["type"] = "internal"
		self.good_body = json.dumps(self.good_body_raw)

	def test_remove_alias_valid(self):
		data = self.good_body
		response = self.client.post('/api/lbalias/add', data, content_type='application/json')
		self.assertEqual(response.status_code, httplib.CREATED)
		response = self.client.delete('/api/lbalias/delete/this_is_a_test_alias-1')
		self.assertEqual(response.status_code, 204)
 
