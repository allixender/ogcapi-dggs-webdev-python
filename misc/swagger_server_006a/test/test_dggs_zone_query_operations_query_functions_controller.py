# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from dggs_api_server.models.distance import Distance  # noqa: E501
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
from dggs_api_server.models.relative_position import RelativePosition  # noqa: E501
from dggs_api_server.test import BaseTestCase


class TestDGGSZoneQueryOperationsQueryFunctionsController(BaseTestCase):
    """DGGSZoneQueryOperationsQueryFunctionsController integration test stubs"""

    def test_dggs_dggs_rsid_zone_zonal_id_child_of_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_child_of_get

        Test if the current ZoneId is childOf another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('inherit_id', false),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/childOf'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_contains_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_contains_get

        Test if the current ZoneId contains another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/contains'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_crosses_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_crosses_get

        Test if the current ZoneId crosses another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/crosses'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_disjoint_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_disjoint_get

        Test if the current ZoneId is disjoint another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/disjoint'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_equals_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_equals_get

        Test if the current ZoneId equals another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/equals'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_intersects_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_intersects_get

        Test if the current ZoneId intersects another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/intersects'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_overlaps_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_overlaps_get

        Test if the current ZoneId overlaps another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/overlaps'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_parent_of_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_parent_of_get

        Test if the current ZoneId is parentOf another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('inherit_id', false),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/parentOf'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_relative_position_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_relative_position_get

        Determine the relativePosition of another ZonalID to the current ZoneId
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/relativePosition'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_sibling_of_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_sibling_of_get

        Test if the current ZoneId is siblingOf another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('inherit_id', false),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/siblingOf'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_touches_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_touches_get

        Test if the current ZoneId touches another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/touches'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_within_distance_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_within_distance_get

        Test if the current ZoneId is withinDistance another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('distance', Distance()),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/withinDistance'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_within_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_within_get

        Test if the current ZoneId within another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/within'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
