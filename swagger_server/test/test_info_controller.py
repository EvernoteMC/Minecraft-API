# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_info_acheivement_get(self):
        """Test case for info_acheivement_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/acheivement',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_biome_get(self):
        """Test case for info_biome_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/biome',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_block_get(self):
        """Test case for info_block_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/block',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_command_get(self):
        """Test case for info_command_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/command',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_item_get(self):
        """Test case for info_item_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/item',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_loottable_get(self):
        """Test case for info_loottable_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/loottable',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_mob_get(self):
        """Test case for info_mob_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/mob',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_structure_get(self):
        """Test case for info_structure_get

        info about a minecraft item
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/info/structure',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
