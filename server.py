import os
from flask import Flask
from flask_restful import Resource, Api
import logging

app = Flask(__name__)
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

class Greeting(Resource):
    def get(self):
        app.logger.info("Received GET request for /")
        return "Clever Cloud is Up & Running!"

api.add_resource(Greeting, '/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
