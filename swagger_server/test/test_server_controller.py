# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServerController(BaseTestCase):
    """ServerController integration test stubs"""

    def test_server_javaicon_get(self):
        """Test case for server_javaicon_get

        
        """
        query_string = [('server', 'server_example'),
                        ('port', 789)]
        response = self.client.open(
            '/v1/server/javaicon',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_servers_bedrock_get(self):
        """Test case for servers_bedrock_get

        
        """
        query_string = [('server', 'server_example'),
                        ('port', 19132)]
        response = self.client.open(
            '/v1/servers/bedrock',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_servers_java_get(self):
        """Test case for servers_java_get

        
        """
        query_string = [('server', 'server_example'),
                        ('port', 25565)]
        response = self.client.open(
            '/v1/servers/java',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
