from flask_restful import Resource

message = "Store-Manager app by Sekidde Derrick"

class Index(Resource):
    def get(self):
        return message