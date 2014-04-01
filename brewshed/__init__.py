from jinja2 import Environment, FileSystemLoader
import os

server_name = '127.0.0.1'
server_port = '8888'

base_url = 'http://{}:{}/'.format(server_name, server_port)

def make_template_env(file):
    directory = os.path.join(os.path.dirname(os.path.abspath(file)), '..', 'templates')
    return Environment(loader=FileSystemLoader(directory), trim_blocks=True)
