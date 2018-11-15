import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v2.db_conn import *
from werkzeug.security import check_password_hash, generate_password_hash
from app.tests.v2.test_app import *

class TestSales(TestProducts):

    def test_post_sales(self):
        response = self.test_client.post('api/v2/sales', data=self.sale_data, headers={
            'content_type': 'application/json', 'access_token': self.storeattendant_token})
        self.assertEqual(response.status_code, 400)
    def test_get_single_sales_admin(self):

        response = self.test_client.get(
            'api/v2/sales/1', headers={'content_type': 'application/json', 'access_token': self.admin_token})

        self.assertEqual(response.status_code, 498)

    def test_get_single_sales_attendant(self):

        response = self.test_client.get('api/v2/sales/1', headers={
                                        'content_type': 'application/json', 'access_token': self.storeattendant_token})
        print(response)

        self.assertEqual(response.status_code, 498)
