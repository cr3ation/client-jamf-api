from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jss

# Create webapp
app = Flask(__name__)
api = Api(app)

# Limitations per host per day / hour
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["500 per day", "20 per hour"])


class Computer(Resource):
    def get(self, serial):
        data = jss.get_computer(serial)
        if not data:
            # Nothing to return
            return("", 204)
        return(data)


class HelloWorld(Resource):
    def get(self):
        return("Hello, World!")


api.add_resource(HelloWorld, "/hello")
api.add_resource(Computer, "/computer/<string:serial>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
