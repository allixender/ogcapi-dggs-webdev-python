# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from dggs_api_server.models.collections import Collections  # noqa: E501
from dggs_api_server.models.conf_classes import ConfClasses  # noqa: E501
from dggs_api_server.models.exception import Exception  # noqa: E501
from dggs_api_server.models.http_response302 import HttpResponse302  # noqa: E501
from dggs_api_server.models.http_response303 import HttpResponse303  # noqa: E501
from dggs_api_server.models.http_response304 import HttpResponse304  # noqa: E501
from dggs_api_server.models.http_response307 import HttpResponse307  # noqa: E501
from dggs_api_server.models.http_response308 import HttpResponse308  # noqa: E501
from dggs_api_server.models.http_response400 import HttpResponse400  # noqa: E501
from dggs_api_server.models.http_response401 import HttpResponse401  # noqa: E501
from dggs_api_server.models.http_response403 import HttpResponse403  # noqa: E501
from dggs_api_server.models.http_response404 import HttpResponse404  # noqa: E501
from dggs_api_server.models.http_response405 import HttpResponse405  # noqa: E501
from dggs_api_server.models.http_response406 import HttpResponse406  # noqa: E501
from dggs_api_server.models.http_response500 import HttpResponse500  # noqa: E501
from dggs_api_server.models.landing_page import LandingPage  # noqa: E501
from dggs_api_server.test import BaseTestCase


class TestOGCAPICommonController(BaseTestCase):
    """OGCAPICommonController integration test stubs"""

    def test_api_get(self):
        """Test case for api_get

        This Document
        """
        query_string = [('f', 'f_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/api',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_get(self):
        """Test case for collections_get

        the collections in a dataset shared from this server
        """
        query_string = [('f', 'f_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_conformance_get(self):
        """Test case for conformance_get

        
        """
        query_string = [('f', 'f_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/conformance',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_describe_collection(self):
        """Test case for describe_collection

        describe a collection
        """
        query_string = [('f', 'f_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}'.format(collection_id='collection_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        landing page
        """
        query_string = [('f', 'f_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
