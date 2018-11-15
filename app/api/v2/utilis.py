import re
from flask import abort,jsonify,make_response
from .models import User, PostProduct

class Registerpass:
    def pass_validate(self, data):

        if not re.search("[A-Z]",data["password"]):
            Response = "password must have an uppercase letter"
            abort(400,Response )

        elif not  re.search("[a-z]",data["password"]):
            Response = "password must have a lowercase letter"
            abort(400,Response )

        elif not re.search("[0-9]",data["password"]):
            Response = "password must have atleast one digit"
            abort(400,Response )

        elif not  re.search("[$#@]",data["password"]):
            Response = "password must have atleast one special character"
            abort(400,Response )

        elif len(data["password"])<6 or len(data["password"])>12:
            Response = "password must  have a minimum of 6 characters"
            abort(400,Response )
    
    def data_validate(self, data):
        if type(data["username"]) is not str or type(data["email"]) is not str or type(data["password"]) is not str or type(data["role"]) is not str :

            Response ="Strings only "

            abort(400, Response)

    def empty_validate(self, data):
        if data["username"] =="" or data["email"] == "" or data["password"] =="" or data["role"] =="" :
            Response ="Enter all details"
            abort(400, Response)

    def space_validate(self,data):
        if " " in data["username"]:
            Response = "Remove space "
            abort(400, Response)
        if " " in data["email"]:
            Response = "Remove space "
            abort(400, Response)

        if " " in data["password"]:
            Response = "Remove space"
            abort(400, Response)
        if " " in data["role"]:
            Response = "Remove space"
            abort(400, Response)

    def existing_user(self,data):
        self.user_ins = User.get_users(self)
        for user in self.user_ins:
            if data["email"] == user["email"]:
                Response="User already exists"
                abort(406,Response)

   
        

