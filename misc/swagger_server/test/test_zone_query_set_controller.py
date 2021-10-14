# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.distance import Distance  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.zone_collection_geo_json import ZoneCollectionGeoJSON  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZoneQuerySetController(BaseTestCase):
    """ZoneQuerySetController integration test stubs"""

    def test_collections_collection_id_zone_zone_id_buffer_get(self):
        """Test case for collections_collection_id_zone_zone_id_buffer_get

        Get the list of zonalId that are within a buffer of dist from the given zoneId
        """
        query_string = [('dist', Distance()),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/buffer'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_child_get(self):
        """Test case for collections_collection_id_zone_zone_id_child_get

        Get the list of zones children of a given zone
        """
        query_string = [('inherit_id', true),
                        ('levels', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/child'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_difference_get(self):
        """Test case for collections_collection_id_zone_zone_id_difference_get

        Get the list of zonalID that are the result of zoneId.difference(another)
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/difference'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_intersection_get(self):
        """Test case for collections_collection_id_zone_zone_id_intersection_get

        Get the list of zonalID that are the result of zoneId.intersection(another)
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/intersection'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_parent_get(self):
        """Test case for collections_collection_id_zone_zone_id_parent_get

        Get the list of zones parents of a given zone
        """
        query_string = [('inherit_id', true),
                        ('levels', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/parent'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_sibling_get(self):
        """Test case for collections_collection_id_zone_zone_id_sibling_get

        Get the list of zones siblings of a given zone
        """
        query_string = [('inherit_id', true),
                        ('levels', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/sibling'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_sym_difference_get(self):
        """Test case for collections_collection_id_zone_zone_id_sym_difference_get

        Get the list of zonalID that are the result of zoneId.symDifference(another)
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/symDifference'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_union_get(self):
        """Test case for collections_collection_id_zone_zone_id_union_get

        Get the list of zonalID that are the result of zoneId.union(another)
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/union'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
