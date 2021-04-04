#! /usr/bin/env python

from collections import OrderedDict
import flask
from flask import Flask, request, Response, jsonify, render_template 
import urllib.parse
import requests

app = flask.Flask(__name__)
app.config['DEBUG'] = False
key = "d6f49dee38b888"
port = 81

@app.route('/', methods=['get'])
def index():

    # -----------------------------------------------
    # Welcome
    # -----------------------------------------------
    return jsonify({"mensagem": "Acesso via /autocomplete?search=ana%20alvarenga%20campos,%20belo%20horizonte"})

@app.route('/autocomplete', methods=['GET'])
def autocomplete():

    # -----------------------------------------------
    # Example request GET
    # /autocomplete?search=ana%20alvarenga%20campos,%20belo%20horizonte
    # -----------------------------------------------

    search = urllib.parse.quote(request.args['search']) #""
    url = "https://api.locationiq.com/v1/autocomplete.php?key="+key+"&q="+search
    response = requests.get(url)

    return Response(response)  

app.run(host="0.0.0.0", port=port)