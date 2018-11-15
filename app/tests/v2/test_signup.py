
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
                "email": "eliud220@gmail.com",
                "password": "Bb#6060",
                "role": "storeattendant"
            })

            
            response = self.test_client.post('api/v2/auth/signup', data=user,headers={
                                                 'content-type': 'application/json', 'access_token': self.admin_token})
        
            print(self.admin_token)                          
            self.assertEqual(response.status_code, 201)