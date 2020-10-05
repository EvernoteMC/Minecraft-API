# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestImagesController(BaseTestCase):
    """ImagesController integration test stubs"""

    def test_images_advancement_get(self):
        """Test case for images_advancement_get

        create a minecraft acheivement
        """
        query_string = [('item', 'cake'),
                        ('title', 'Achievement Got:'),
                        ('text', 'text_example')]
        response = self.client.open(
            '/v1/images/advancement',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_images_book_get(self):
        """Test case for images_book_get

        create a page from a minecraft book
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/images/book',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_images_death_get(self):
        """Test case for images_death_get

        Create a custom death screen
        """
        query_string = [('message', 'message_example'),
                        ('xp', 56)]
        response = self.client.open(
            '/v1/images/death',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_images_motd_get(self):
        """Test case for images_motd_get

        View motd
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/images/motd',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_images_sign_get(self):
        """Test case for images_sign_get

        create an sign.png
        """
        query_string = [('wood', 'oak'),
                        ('line1', 'line1_example'),
                        ('line2', 'line2_example'),
                        ('line3', 'line3_example'),
                        ('line4', 'line4_example')]
        response = self.client.open(
            '/v1/images/sign',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_images_splashscreen_get(self):
        """Test case for images_splashscreen_get

        Create a custom minecraft splashscreen
        """
        query_string = [('text', 'text_example')]
        response = self.client.open(
            '/v1/images/splashscreen',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
