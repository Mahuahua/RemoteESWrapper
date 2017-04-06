
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import gevent
import json
import requests
import flask
from flask import Flask,  request, jsonify, _app_ctx_stack

import flask_restful
from flask_restful import abort, Api, Resource
from flask_cors import CORS



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
    Custom git repository search from remote ES
    """
    def get(self):
        query = request.args.get('query')

        url = "http://localhost:9200/repo-search/_search"
        payload = "{\n    \"query\": {\n        \"bool\" : {\n            \"must\" : {\n                \"query_string\" : {\n                    \"query\" : \"UserInput\"\n                }\n            }\n        }\n    }\n}"
        payload = payload.replace("UserInput", query)
        print(payload)
        response = requests.request("POST", url, data=payload)

        print(response.json())

        return response.json(), 200

    def delete(self):
        return '', 405

    def put(self):
        return '', 405

    def post(self):
        return '', 405

    def delete(self):
        return '', 405

class RepoSearch(Resource):
    """
    Custom git repository search from remote ES
    """
    def get(self):
        query = request.args.get('query')
        searchIn = request.args.get('searchIn')
        url = 'https://api.github.com/search/repositories?q=WTF+user:mahuahua'
        url = url.replace("WTF", query)
        if searchIn:
            url = url + '+in:' + searchIn.strip()

        response = requests.request("GET", url)
        jsonresponse = response.json()
        returnjson = {}
        returnjson['hit_count'] = jsonresponse.get('total_count')
        hits = []
        for hit in jsonresponse.get('items'):
            repo = {}
            repo['url'] = hit.get('html_url')
            repo['name'] = hit.get('name')
            repo['description'] = hit.get('description')
            repo['updated_at'] = hit.get('updated_at')
            hits.append(repo)
        returnjson['hits'] = hits
        return returnjson, 200

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
CORS(app)
port = int(os.getenv("PORT", 8049))


def bootstrap():
    # Define resources
    api.add_resource(ElasticSearch, '/es')
    api.add_resource(RepoSearch, '/repo')

if __name__ == '__main__':
    bootstrap()
    app.run(host='0.0.0.0', port=port, debug=True)
