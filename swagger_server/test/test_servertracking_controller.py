# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestServertrackingController(BaseTestCase):
    """ServertrackingController integration test stubs"""

    def test_strack_delete(self):
        """Test case for strack_delete

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/strack',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_strack_get(self):
        """Test case for strack_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/strack',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_strack_post(self):
        """Test case for strack_post

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/strack',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_strack_put(self):
        """Test case for strack_put

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/strack',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
