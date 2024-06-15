import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return "Clever Cloud is Up & Running!"

api.add_resource(Greeting, '/')

if __name__ == '__main__':
    # Use os.environ.get("PORT", 8080) to get the port number from environment variable
    port = int(os.environ.get("PORT", 8080))
    # Use host="0.0.0.0" to listen on all network interfaces
    app.run(host="0.0.0.0", port=port)
