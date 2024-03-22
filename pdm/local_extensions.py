from platform import python_version

from jinja2.ext import Extension


class PythonVersionExtension(Extension):
    def __init__(self, environment):
        super(PythonVersionExtension, self).__init__(environment)
        environment.globals["python_version"] = python_version()