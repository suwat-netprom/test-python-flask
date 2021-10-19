from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        i = 5
        j = 5
        x = i + j
        return {'message': 'Hello World'}