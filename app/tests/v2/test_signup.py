
import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v2.db_conn import *
from werkzeug.security import check_password_hash, generate_password_hash
from app.tests.v2.test_app import *



class Testsignup(TestProducts):
    def test_signup(self):
            users_data_admin = json.dumps({
                "username": "Winnie",
                "email": "winniekariuki07@gmail.com",
                "password": "winnie07@",
                "role": "Admin"


            })
            self.create_admin_user = self.test_client.post('api/v2/auth/signup', data=users_data_admin,
                                                                content_type='application/json')


            self.login_admin_user = self.test_client.post(
                '/api/v2/auth/login', data=self.login_data_admin, content_type='application/json')



            user = json.dumps({
                "username": "Eliud",
                "email": "eliud280@gmail.com",
                "password": "Bb#6060",
                "role": "storeattendant"
            })

            
            response = self.test_client.post('api/v2/auth/signup', data=user,headers={
                                                 'content-type': 'application/json', 'access_token': self.admin_token['token']})
        
            # print(self.admin_token)                          
            self.assertEqual(response.status_code, 201)