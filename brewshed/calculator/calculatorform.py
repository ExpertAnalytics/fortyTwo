
class FormDataItem(object):
    """
    Ordered dict
    """

    def __init__(self, key, val, pos):
        self.key = key
        self.val = val
        self.pos = pos


class HTMLFormData(object):

    def controller(self, name):
        controller_name = '{}Ctrl'.format(name)
        script = """
        <script>
            function {0}($scope) {
                $scope.HTMLForm = {};
                var formData = {
                }
                $scope.HTMLForm.submitTheForm = function(item, event) {
                var responsePromise = $http.post("/calculate/"+$scope.calculatorForm.calculator_id+"/", formData, {});
                responsePromise.success(function(dataFromServer, status, headers, config) {
                    $scope.calculatorUri = dataFromServer.form_uri;
                    $scope.calculatorLinkText = dataFromServer.name;
                    $scope.formSubmitted = true;
                });
                responsePromise.error(function(data, status, headers, config) {
                    alert("Submitting form failed!");
                });
                }
            }
        </script>
        """.format(controller_name)

        return script, controller_name

    def generate(self, name='HTMLForm'):
        assert hasattr(self, 'data')
        script, controller_name = self.controller(name)
        html = """
        <div ng-controller="{}">
            <form>""".format(controller_name)
        for k,v in self.content:
            html += "<input type='text' name='k' ng-model=''>"

        html += """
        <button ng-click="">Calculate</button>
        </form>
        </div>
        """

        return script+html


class CalculatorFormData(HTMLFormData):

    def __init__(self, **kwargs):
        self.content = kwargs