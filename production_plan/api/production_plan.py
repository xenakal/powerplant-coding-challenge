import logging
from flask import Flask, request
from flask_api import status
from flask_restful import Resource, Api
from flask_expects_json import expects_json
from flask_socketio import SocketIO
import powerplant_manager as manager
from payload_parser import PayloadParser

# TODO: put this in config file 
HOST = '0.0.0.0'
PORT = '8888'

def create_production_plan_app(config=None):
    """ Creates the production plan flask api, along with the websocket. """
    logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s : %(message)s')

    app = Flask(__name__)
    socket = SocketIO()
    api = Api()
    api.add_resource(ProductionPlan, '/productionplan')
    return app, api, socket

def run_production_plan_app(app, api, socket):
    """ Runs the provided api and socket."""
    api.init_app(app)
    socket.init_app(app) 
    socket.run(app, port=PORT) 

class ProductionPlan(Resource):
    @expects_json(PayloadParser.PAYLOAD_SCHEMA)
    def post(self):
        post_data = request.get_json()
        app.logger.info("POST received")
        payload_parser = PayloadParser(post_data, app.logger)
        production_plan = manager.get_optimal_powerplants_for_load(payload_parser, app.logger)
        to_emit = dict(input=post_data, output=production_plan)
        socket.emit('production_plan', {'production_plan': to_emit}, broadcast=True)
        return production_plan, status.HTTP_200_OK

if __name__ == "__main__":
    app, api, socket = create_production_plan_app()
    run_production_plan_app(app, api, socket)
    
