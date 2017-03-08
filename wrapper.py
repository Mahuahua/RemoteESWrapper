# curl -X POST -H "Authorization: Basic Z2l0aHVidXNlcjpnaXRodWI=" -H "Cache-Control: no-cache" -H "Postman-Token: 843590f3-9ba3-1158-b39e-5e5800a593d0" -d '{
#     "query": {
#         "bool" : {
#             "
#                 "query_string" : {
#                     "query" : "pascal"
#                 }
#             }
#         }
#     }
# }' "http://ec2-34-199-166-215.compute-1.amazonaws.com:9200/repo-search/repo/_search"

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import gevent
import json

import flask
from flask import Flask,  request, jsonify, _app_ctx_stack

import flask_restful
from flask_restful import abort, Api, Resource



__version__ = '0.1'


def bootstrap():
    return

def handle_error(error, status_code):
    """
    Format error response and append status code.
    """
    resp = jsonify(error)
    resp.status_code = status_code
    return resp

class ElasticSearch(Resource):
    """
    1. <service root>/parse - parse a given sentence (examples below)
    """
    def get(self):
        query = request.args.get('query')
        return query, 200

    def delete(self):
        return '', 405

    def put(self):
        return '', 405

    def post(self):
        return '', 405

    def delete(self):
        return '', 405

app = Flask(__name__)
api = Api(app)
port = int(os.getenv("PORT", 8049))


def bootstrap():
    # Define resources
    api.add_resource(ElasticSearch, '/es')

if __name__ == '__main__':
    bootstrap()
    app.run(host='0.0.0.0', port=port, debug=True)
