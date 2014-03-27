import webapp2
from jinja2 import Environment, FileSystemLoader
from paste import httpserver
from paste.cascade import Cascade
from paste.urlparser import StaticURLParser
import os

THIS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
template_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

class StrikeWaterTemperatureHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(template_env.get_template('strikewater.html').render(
            type='grain mass')
        )


class AboutHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write('<html>This portal is made to scratch my personal itching :)</html>')


web_app = webapp2.WSGIApplication(
    [('/', StrikeWaterTemperatureHandler),
     ('/about/', AboutHandler)
    ],
    debug=True)

static_app = StaticURLParser("brewshed/calculator/static/")

app = Cascade([web_app, static_app])

def main():
    httpserver.serve(app, host='127.0.0.1', port='8888')

if __name__ == '__main__':
    main()
