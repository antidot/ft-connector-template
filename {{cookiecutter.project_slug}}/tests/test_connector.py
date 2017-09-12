from io import BytesIO
from zipfile import ZipFile

from fluid.api.v2 import PublicationBuilder
from fluid.api.v2.test_helpers.fake_client import FakeClient
from {{cookiecutter.project_slug}}.connector import {{cookiecutter.class_name}}


def test_connector():
    client = FakeClient()
    conf = {}

    connector = {{cookiecutter.class_name}}(client, conf)

    with ZipFile(BytesIO(), 'w') as data_test:
        data_test.writestr('test.map', b'foo')

        connector.transform(data_test)

        client.assert_that_published_publications_are(
            PublicationBuilder().id('test').title('Foo').lang('en-US').build()
        )
