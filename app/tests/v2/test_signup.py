import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v2.db_conn import *
from werkzeug.security import check_password_hash, generate_password_hash
from app.tests.v2.test_app import *



class Testsignup(TestProducts):
    def test_signup(self):

        user = json.dumps({
            "username": "Eliud",
            "email": "eliud825@gmail.com",
            "password": "Bb#6060",
            "role": "storeattendant"
        })

        
        response = self.test_client.post('api/v2/auth/signup', data=user,
                                          content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
    def test_login(self):
        login = json.dumps({
            "email": "eliud825@gmail.com",
            "password": "Bb#6060"
        })
        response = self.test_client.post(
            '/api/v2/auth/login', data=login, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    def test_get_users(self):

        response = self.test_client.get(
            'api/v2/users', content_type='application/json')
        self.assertEqual(response.status_code, 200)


            
        
          