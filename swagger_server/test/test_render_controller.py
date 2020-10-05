# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestRenderController(BaseTestCase):
    """RenderController integration test stubs"""

    def test_render_banner_get(self):
        """Test case for render_banner_get

        View motd
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/render/banner',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_render_firework_get(self):
        """Test case for render_firework_get

        View motd
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/render/firework',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_render_item_get(self):
        """Test case for render_item_get

        View motd
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/render/item',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_render_mob_get(self):
        """Test case for render_mob_get

        View motd
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/render/mob',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_render_recipie_get(self):
        """Test case for render_recipie_get

        View motd
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/render/recipie',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
