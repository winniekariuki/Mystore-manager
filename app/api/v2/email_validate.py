import re
from flask import abort,jsonify,make_response
from .models import User

class Registeremail:
    def email_validate(self, data):
        if  re.search("[A-Z]",data["email"]):
            Response = "No uppercase in email"
            abort(400,Response )

        elif not  re.search("[a-z]",data["email"]):
            Response = "email must have  lowercase letters"
            abort(400,Response )

        elif not re.search("[0-9]",data["email"]):
            Response = "email must have atleast one digit"
            abort(400,Response )

        elif not  re.search("[@]",data["email"]):
            Response = "email must have @ special case"
            abort(400,Response )
        elif not re.search("[.]", data["email"]):
            Response = "email must have [.] "
            abort(400,Response )  
        elif len(data["email"])<6 or len(data["email"])>30:
            Response = "email must  have a minimum of 6 characters"
            abort(400,Response )
