"""
VyPR analysis library.
Authors:
Marta Han - University of Zagreb, CERN
Joshua Dawes - University of Manchester, CERN.
"""
import json
import requests
import urllib2
from datetime import datetime
import pickle
from graphviz import Digraph
from pprint import pprint
import sys
import ast

from VyPRAnalysis.http_requests import VerdictServerConnection

config_dict = None
server_url = None
connection = None
vypr_path = "VyPRAnalysis"

sys.path.append(vypr_path)

def set_config_file(config_file_name='config.json'):
    """
    Given config_file_name, read the configuration.
    """
    global config_dict, server_url
    config_dict = json.loads(open(config_file_name))
    server_url = config_dict["verdict_server_url"]

def set_server(given_url):
    """
    server_url is a global variable which can be changed
    by passing a string to the set_server() function
    """
    global server_url, connection
    server_url=given_url
    # try to connect
    connection = VerdictServerConnection(server_url)
    try:
        response = connection.handshake()
    except:
        print("Failed to connect to server.")

def get_server():
    global server_url
    return server_url

def get_connection():
    global connection
    # try the handshake
    response = connection.handshake()
    return connection

def set_vypr_path(path):
    global vypr_path
    vypr_path = path
    sys.path.append(vypr_path)


"""
Import all functions from various modules.
"""

from utils import *
from orm import *
 