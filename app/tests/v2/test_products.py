import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v2.db_conn import *
from werkzeug.security import check_password_hash, generate_password_hash
from app.tests.v2.test_app import *

class TestGood(TestProducts):
    def test_create_product(self):
        product_data = json.dumps({
            "name": "itel825",
            "category": "mobile",
            "price": 2563,
            "quantity": 2,
            "lower_inventory": 10
        })
        response = self.test_client.post('api/v2/products', data=product_data,
                                         content_type='application/json')
        print(response.data)

        self.assertEqual(response.status_code, 201)
    def test_get_products(self):

        response = self.test_client.get(
            'api/v2/products', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_products_by_id(self):

        response = self.test_client.get(
            'api/v2/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    def test_delete_product(self):
        response = self.test_client.get(
            'api/v2/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_put_product(self):

        response = self.test_client.get(
            'api/v2/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
