import re
from flask import abort,jsonify,make_response
from .models import  PostProduct

class Validateproduct:

    def emptydetails(self, data):
        if data["name"] == "":
            Response = "Details required"
            abort(400, Response)
        if data["category"] == "":
            Response = "Details required"
            abort(400, Response)
        if data["price"] == "":
            Response = "Details required"
            abort(400, Response)
        if  data["quantity"] == "":
            Response = "Details required"
            abort(400, Response)

        if  data["lower_inventory"] == "":
            Response = "Details required"
            abort(400, Response)
    def existing_product(self,data):
        self.product_ins = PostProduct.get_products(self)
        for product in self.product_ins:
            if data["name"] == product["name"]:
                Response="product already exists"
                abort(406,Response)
