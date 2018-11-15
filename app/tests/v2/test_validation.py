import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v2.db_conn import *
from werkzeug.security import check_password_hash, generate_password_hash
from app.tests.v2.test_app import *

class TestValidation(TestProducts):
    def test_password_lowercase(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "halim07@gmail.com",
            "password": "A@5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have a lowercase letter")
        self.assertEqual(response.status_code, 400)

    def test_password_uppercase(self):
        user = json.dumps({
            "username": "Harrjhgiet",
            "email": "fahkjhkh4@.com",
            "password": "a@5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have an uppercase letter")
        self.assertEqual(response.status_code, 400)

    def test_password_digit(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "sfah7@g.com",
            "password": "a@Afff",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have atleast one digit")
        self.assertEqual(response.status_code, 400)

    def test_password_special_char(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "safhah4@gm.com",
            "password": "a1Afff",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have atleast one special character")
        self.assertEqual(response.status_code, 400)

    def test_password_length(self):
        user = json.dumps({
            "username": "Hargfhmjriet",
            "email": "aehgjklkfg2@.com",
            "password": "a1A@",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})

        self.assertEqual(json.loads(response.data)
                         ['message'], "password must  have a minimum of 6 characters")
        self.assertEqual(response.status_code, 400)

    def test_empty_username(self):
        user = json.dumps({
            "username": "",
            "email": "aefg2@.com",
            "password": "Aa1@ffff",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Enter all details")
        self.assertEqual(response.status_code, 400)

    def test_empty_password(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "aefg2@.com",
            "password": "",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Enter all details")
        self.assertEqual(response.status_code, 400)

    def test_empty_role(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "harriet7@gmail.com",
            "password": "Aa1@ffff",
            "role": ""})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Enter all details")
        self.assertEqual(response.status_code, 400)

    def test_empty_space_role(self):
        user = json.dumps({
            "username": "Harrgfhjkiet",
            "email": "ayhtgjkjefg2@.com",
            "password": "Aa1@ffff",
            "role": "Ad min"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Remove space")
        self.assertEqual(response.status_code, 400)

    def test_empty_space_password(self):
        user = json.dumps({
            "username": "Hajklk;lrriet",
            "email": "aefhgjklg2@.com",
            "password": "Aa1 @ffff",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Remove space")
        self.assertEqual(response.status_code, 400)

    def test_email_lowercase(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "HALIM07@gmail.com",
            "password": "A@p5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "No uppercase in email")
        self.assertEqual(response.status_code, 400)

    def test_email_digit(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "sedftg@gmail.com",
            "password": "A@p5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "email must have atleast one digit")
        self.assertEqual(response.status_code, 400)

    def test_special_case(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "sedftg4gmail.com",
            "password": "A@p5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "email must have @ special case")
        self.assertEqual(response.status_code, 400)

    def test_dot(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "sedftg4@gmailcom",
            "password": "A@p5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "email must have [.] ")
        self.assertEqual(response.status_code, 400)

    def test_len(self):
        user = json.dumps({
            "username": "Harriet",
            "email": "g4@.c",
            "password": "A@p5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v2/auth/signup", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "email must  have a minimum of 6 characters")
        self.assertEqual(response.status_code, 400)

    def test_product_exists(self):
        product_data = json.dumps({
            "name": "itel823",
            "category": "Laptop",
            "price": 2563,
            "quantity": 2,
            "lower_inventory": 10
        })
        response = self.test_client.post('api/v2/products', data=product_data, headers={
            'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "product already exists")
        self.assertEqual(response.status_code, 406)

    def test_empty_products(self):
        product_data = json.dumps({
            "name": "",
            "category": "Laptop",
            "price": 2563,
            "quantity": 2,
            "lower_inventory": 10
        })
        response = self.test_client.post('api/v2/products', data=product_data, headers={
            'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Details required")
        self.assertEqual(response.status_code, 400)


