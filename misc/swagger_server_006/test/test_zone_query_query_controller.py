# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.distance import Distance  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.relative_position import RelativePosition  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZoneQueryQueryController(BaseTestCase):
    """ZoneQueryQueryController integration test stubs"""

    def test_collections_collection_id_zone_zone_id_child_of_get(self):
        """Test case for collections_collection_id_zone_zone_id_child_of_get

        Test if the current ZoneId is childOf another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('inherit_id', true),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/childOf'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_contains_get(self):
        """Test case for collections_collection_id_zone_zone_id_contains_get

        Test if the current ZoneId contains another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/contains'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_crosses_get(self):
        """Test case for collections_collection_id_zone_zone_id_crosses_get

        Test if the current ZoneId crosses another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/crosses'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_disjoint_get(self):
        """Test case for collections_collection_id_zone_zone_id_disjoint_get

        Test if the current ZoneId is disjoint another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/disjoint'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_equals_get(self):
        """Test case for collections_collection_id_zone_zone_id_equals_get

        Test if the current ZoneId equals another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/equals'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_intersects_get(self):
        """Test case for collections_collection_id_zone_zone_id_intersects_get

        Test if the current ZoneId intersects another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/intersects'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_overlaps_get(self):
        """Test case for collections_collection_id_zone_zone_id_overlaps_get

        Test if the current ZoneId overlaps another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/overlaps'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_parent_of_get(self):
        """Test case for collections_collection_id_zone_zone_id_parent_of_get

        Test if the current ZoneId is parentOf another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('inherit_id', true),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/parentOf'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_relative_position_get(self):
        """Test case for collections_collection_id_zone_zone_id_relative_position_get

        Determine the relativePosition of another ZonalID to the current ZoneId
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/relativePosition'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_sibling_of_get(self):
        """Test case for collections_collection_id_zone_zone_id_sibling_of_get

        Test if the current ZoneId is siblingOf another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('inherit_id', true),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/siblingOf'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_touches_get(self):
        """Test case for collections_collection_id_zone_zone_id_touches_get

        Test if the current ZoneId touches another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/touches'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_within_distance_get(self):
        """Test case for collections_collection_id_zone_zone_id_within_distance_get

        Test if the current ZoneId is withinDistance another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('dist', Distance()),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/withinDistance'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_within_get(self):
        """Test case for collections_collection_id_zone_zone_id_within_get

        Test if the current ZoneId within another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/within'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
