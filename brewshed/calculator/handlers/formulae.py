from brewshed.handler import BrewshedHandler
from brewshed.handler import template
import httplib
import json
from brewshed import make_template_env
from brewshed import base_url

template_env = make_template_env(__file__)

calculator_mocks = [
    {'id': 0, 'name': 'Strike Water Temperature', 'form_uri': '{}swt/'.format(base_url)},
    {'id': 1, 'name': 'Water Amount', 'form_uri': '{}wa/'.format(base_url)}
]

class WelcomeHandler(BrewshedHandler):

    @template('index.html')
    def get(self):
        pass


class CalculatorHandler(BrewshedHandler):

    @template('calculator.html')
    def get(self):
        return dict(calculators=calculator_mocks)
        #self.response.write(template_env.get_template('calculator.html').render(
        #    calculators=calculator_mocks))

    def post(self, calculator_id):
        id = int(calculator_id)

        ids = [calc['id'] for calc in calculator_mocks]
        if id not in ids:
            self.response.abort(httplib.NOT_FOUND)
        calculator = [calc for calc in calculator_mocks if calc['id'] == int(calculator_id)][0]
        self.response.write(json.dumps(calculator))


class AboutHandler(BrewshedHandler):

    @template('about.html')
    def get(self):
        pass

