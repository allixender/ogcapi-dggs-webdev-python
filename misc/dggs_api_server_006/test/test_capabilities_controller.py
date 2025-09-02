# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from dggs_api_server.models.collection_list import CollectionList  # noqa: E501
from dggs_api_server.models.conf_classes import ConfClasses  # noqa: E501
from dggs_api_server.models.exception import DggsException  # noqa: E501
from dggs_api_server.models.landing_page import LandingPage  # noqa: E501
from dggs_api_server.test import BaseTestCase


class TestCapabilitiesController(BaseTestCase):
    """CapabilitiesController integration test stubs"""

    def test_collections_get(self):
        """Test case for collections_get

        the list of supported collections
        """
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_conformance_get(self):
        """Test case for conformance_get

        information about specifications that this API conforms to (we may not need one)
        """
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/conformance',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        landing page
        """
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
