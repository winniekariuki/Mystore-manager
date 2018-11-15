import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v2.db_conn import *
from werkzeug.security import check_password_hash, generate_password_hash


class TestProducts(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        dbconn()
        destroy_tables()
        create_tables()
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        product_data = json.dumps({
            "name": "del",
            "category": "Laptop",
            "price": 2563,
            "quantity": 23,
            "lower_inventory": 10
        })

        users_data_storeattendant = json.dumps({
            "username": "Sammy",
            "email": "sammy0fgh10@gmail.com",
            "password": "aS@1244",
            "role": "storeattendant"

        })
        self.login_data_storeattendant = json.dumps({
            "email": "sammy0fgh10@gmail.com",
            "password": "aS@1244"

        })

        self.login_data_admin = json.dumps({
            "email": "winniekariuki07@gmail.com",
            "password": "winnie07@"

        })
        self.sale_data = json.dumps({
            "name": "del",
            "quantity": 1
        })

        self.login_admin_user = self.test_client.post(
            '/api/v2/auth/login', data=self.login_data_admin, content_type='application/json')

        print(self.login_admin_user.data)
        self.admin_token = json.loads(
            self.login_admin_user.data.decode())

        self.create_storeattendant_user = self.test_client.post('api/v2/auth/signup', data=users_data_storeattendant,
                                                                content_type='application/json')

        self.login_attendant_user = self.test_client.post(
            '/api/v2/auth/login', data=self.login_data_storeattendant, content_type='application/json')
        self.storeattendant_token = json.loads(
            self.login_attendant_user.data.decode())
        # print(self.login_attendant_user.data)

        self.create_product = self.test_client.post('api/v2/products', data=product_data,
                                                    content_type='application/json')

        self.create_sale = self.test_client.post('api/v2/sales', data=self.sale_data, headers={
                                                 'content-type': 'application/json', 'access_token': self.storeattendant_token})
        
      
    def tearDown(self):
        destroy_tables()

        self.app_context.pop()

    

   