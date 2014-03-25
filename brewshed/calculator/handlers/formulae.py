import webapp2
from jinja2 import FileSystemLoader

class StrikeWaterTemperatureHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(FileSystemLoader('/templates').load('strikewater.html'))


class AboutHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write('<html>This portal is made to scratch my personal itching :)</html>')


app = webapp2.WSGIApplication(
    [('/', StrikeWaterTemperatureHandler),
     ('/about/', AboutHandler)
    ],
    debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8888')

if __name__ == '__main__':
    main()
