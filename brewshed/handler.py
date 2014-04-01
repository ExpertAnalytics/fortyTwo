from webapp2 import RequestHandler
import inspect
from brewshed import make_template_env
from functools import wraps
import os

def template(template_name):

    def decorator(method):

        @wraps(method)
        def wrapper(handler, *args, **kwargs):
            file = inspect.getfile(handler.__class__)
            print file
            template_env = make_template_env(file)
            response = method(handler, *args, **kwargs)
            if isinstance(response, dict):
                handler.response.write(template_env.get_template(template_name).render(**response))
            else:
                handler.response.write(template_env.get_template(template_name).render())
        return wrapper
    return decorator

class BrewshedHandler(RequestHandler):
    pass
