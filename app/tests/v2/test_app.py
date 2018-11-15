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

    

    # 

    # def test_login(self):
    #     login = json.dumps({
    #         "email": "eliud400@gmail.com",
    #         "password": "Bb#6060"
    #     })
    #     response = self.test_client.post(
    #         '/api/v2/auth/login', data=login, content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_products(self):

    #     response = self.test_client.get(
    #         'api/v2/products', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_products_by_id(self):

    #     response = self.test_client.get(
    #         'api/v2/products/1', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_users(self):

    #     response = self.test_client.get(
    #         'api/v2/users', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # # def test_get_sales(self):

    # #     response = self.test_client.get(
    # #         'api/v2/sales', content_type='application/json')
    # #     self.assertEqual(response.status_code, 200)

    # def test_delete_product(self):

    #     response = self.test_client.get(
    #         'api/v2/products/1', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_put_product(self):

    #     response = self.test_client.get(
    #         'api/v2/products/1', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_password_lowercase(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "halim07@gmail.com",
    #         "password": "A@5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "password must have a lowercase letter")
    #     self.assertEqual(response.status_code, 400)

    # def test_password_uppercase(self):
    #     user = json.dumps({
    #         "username": "Harrjhgiet",
    #         "email": "fahkjhkh4@.com",
    #         "password": "a@5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "password must have an uppercase letter")
    #     self.assertEqual(response.status_code, 400)

    # def test_password_digit(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "sfah7@g.com",
    #         "password": "a@Afff",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "password must have atleast one digit")
    #     self.assertEqual(response.status_code, 400)

    # def test_password_special_char(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "safhah4@gm.com",
    #         "password": "a1Afff",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "password must have atleast one special character")
    #     self.assertEqual(response.status_code, 400)

    # def test_password_length(self):
    #     user = json.dumps({
    #         "username": "Hargfhmjriet",
    #         "email": "aehgjklkfg2@.com",
    #         "password": "a1A@",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})

    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "password must  have a minimum of 6 characters")
    #     self.assertEqual(response.status_code, 400)

    # def test_empty_username(self):
    #     user = json.dumps({
    #         "username": "",
    #         "email": "aefg2@.com",
    #         "password": "Aa1@ffff",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Enter all details")
    #     self.assertEqual(response.status_code, 400)

    # def test_empty_password(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "aefg2@.com",
    #         "password": "",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Enter all details")
    #     self.assertEqual(response.status_code, 400)

    # def test_empty_role(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "harriet7@gmail.com",
    #         "password": "Aa1@ffff",
    #         "role": ""})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Enter all details")
    #     self.assertEqual(response.status_code, 400)

    # def test_empty_space_role(self):
    #     user = json.dumps({
    #         "username": "Harrgfhjkiet",
    #         "email": "ayhtgjkjefg2@.com",
    #         "password": "Aa1@ffff",
    #         "role": "Ad min"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Remove space")
    #     self.assertEqual(response.status_code, 400)

    # def test_empty_space_password(self):
    #     user = json.dumps({
    #         "username": "Hajklk;lrriet",
    #         "email": "aefhgjklg2@.com",
    #         "password": "Aa1 @ffff",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Remove space")
    #     self.assertEqual(response.status_code, 400)

    # def test_email_lowercase(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "HALIM07@gmail.com",
    #         "password": "A@p5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "No uppercase in email")
    #     self.assertEqual(response.status_code, 400)

    # def test_email_digit(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "sedftg@gmail.com",
    #         "password": "A@p5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "email must have atleast one digit")
    #     self.assertEqual(response.status_code, 400)

    # def test_special_case(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "sedftg4gmail.com",
    #         "password": "A@p5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "email must have @ special case")
    #     self.assertEqual(response.status_code, 400)

    # def test_dot(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "sedftg4@gmailcom",
    #         "password": "A@p5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "email must have [.] ")
    #     self.assertEqual(response.status_code, 400)

    # def test_len(self):
    #     user = json.dumps({
    #         "username": "Harriet",
    #         "email": "g4@.c",
    #         "password": "A@p5050",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v2/auth/signup", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "email must  have a minimum of 6 characters")
    #     self.assertEqual(response.status_code, 400)

    # def test_product_exists(self):
    #     product_data = json.dumps({
    #         "name": "itel400",
    #         "category": "Laptop",
    #         "price": 2563,
    #         "quantity": 2,
    #         "lower_inventory": 10
    #     })
    #     response = self.test_client.post('api/v2/products', data=product_data, headers={
    #         'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "product already exists")
    #     self.assertEqual(response.status_code, 406)

    # def test_empty_products(self):
    #     product_data = json.dumps({
    #         "name": "",
    #         "category": "Laptop",
    #         "price": 2563,
    #         "quantity": 2,
    #         "lower_inventory": 10
    #     })
    #     response = self.test_client.post('api/v2/products', data=product_data, headers={
    #         'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Details required")
    #     self.assertEqual(response.status_code, 400)

    # def test_post_sales(self):
    #     response = self.test_client.post('api/v2/sales', data=self.sale_data, headers={
    #         'content_type': 'application/json', 'access_token': self.storeattendant_token})

    #     self.assertEqual(response.status_code, 400)

    # # def test_get_single_sales_admin(self):

    # #     response = self.test_client.get(
    # #         'api/v2/sales/1', headers={'content_type': 'application/json', 'access_token': self.admin_token})

    # #     self.assertEqual(response.status_code, 200)

    # # def test_get_single_sales_attendant(self):

    # #     response = self.test_client.get('api/v2/sales/1', headers={
    # #                                     'content_type': 'application/json', 'access_token': self.storeattendant_token})
    # #     print(response)

    # #     self.assertEqual(response.status_code, 200)
