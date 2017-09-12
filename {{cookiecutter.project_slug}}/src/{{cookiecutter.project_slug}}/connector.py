from zipfile import ZipFile

from fluid.api.v2 import Connector, Client


class {{cookiecutter.class_name}}(Connector):
    def __init__(self, client: Client, configuration: dict):
        self.client = client
        self.configuration = configuration

    def transform(self, zipfile: ZipFile):
        pass
