from webapp2 import WSGIApplication
from webapp2 import Route
from paste.cascade import Cascade
from paste.urlparser import StaticURLParser


web_app = WSGIApplication(
    [
        Route('/',
              'brewshed.calculator.handlers.formulae.WelcomeHandler',
              methods=('GET',)),
        Route('/calculator/',
              'brewshed.calculator.handlers.formulae.CalculatorHandler',
              name='calculator',
              methods=('GET',)),
        Route('/calculator/<calculator_id>/',
              'brewshed.calculator.handlers.formulae.CalculatorHandler',
              name='calculator',
              methods=('POST',)),
        Route('/about/',
              'brewshed.calculator.handlers.formulae.AboutHandler',
              name='about',
              methods=('GET',)),
        Route('/calculator/swt/',
              'brewshed.calculator.handlers.formulae.StrikeWaterHandler',
              name='swt',
              methods=('GET','POST')),
        Route('/calculator/wa/',
              'brewshed.calculator.handlers.formulae.WaterAmountHandler',
              name='wa',
              methods=('GET','POST')),
    ],
    debug=True)


static_app = StaticURLParser("brewshed/calculator/static/")
app = Cascade([web_app, static_app])

