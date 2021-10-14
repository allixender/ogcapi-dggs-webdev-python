# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.collection import Collection  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.zone_collection_geo_json import ZoneCollectionGeoJSON  # noqa: E501
from swagger_server.models.zone_geo_json import ZoneGeoJSON  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDGGSAccessController(BaseTestCase):
    """DGGSAccessController integration test stubs"""

    def test_collections_collection_id_describe_get(self):
        """Test case for collections_collection_id_describe_get

        Describes a particular DGGS
        """
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/describe'.format(collection_id='collection_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_get(self):
        """Test case for collections_collection_id_zone_get

        Access the definition of a particular zone
        """
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone'.format(collection_id='collection_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zones_get(self):
        """Test case for collections_collection_id_zones_get

        Access the list of zones in a given DGGS. Can list either all the zones, or a particular subset based on resolution, WGS84 bbox, or list of containing zones (e.g., polygon defined in DGGS terms)
        """
        query_string = [('resolution', 1.2),
                        ('bbox', 3.4),
                        ('zone_id_list', 'zone_id_list_example'),
                        ('limit', 10000)]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zones'.format(collection_id='collection_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
