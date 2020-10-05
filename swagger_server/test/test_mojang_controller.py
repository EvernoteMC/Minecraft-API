# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMojangController(BaseTestCase):
    """MojangController integration test stubs"""

    def test_mojang_check_get(self):
        """Test case for mojang_check_get

        Get information on mojang services
        """
        response = self.client.open(
            '/v1/mojang/check',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
