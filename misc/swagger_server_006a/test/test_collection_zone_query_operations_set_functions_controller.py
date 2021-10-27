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
from dggs_api_server.models.zone_collection_geo_json import ZoneCollectionGeoJSON  # noqa: E501
from dggs_api_server.test import BaseTestCase


class TestCollectionZoneQueryOperationsSetFunctionsController(BaseTestCase):
    """CollectionZoneQueryOperationsSetFunctionsController integration test stubs"""

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_buffer_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_buffer_get

        Get the list of zonalId that are within a buffer of dist from the given zoneId within a Collection
        """
        query_string = [('dist', Distance()),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/buffer'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example', zonal_id='zonal_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_child_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_child_get

        Get the list of zones children of a given zone  within a Collection
        """
        query_string = [('inherit_id', false),
                        ('levels', 1),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/child'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example', zonal_id='zonal_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_difference_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_difference_get

        Get the list of zonalID that are the result of zoneId.difference(another)  within a Collection
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/difference'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_intersection_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_intersection_get

        Get the list of zonalID that are the result of zoneId.intersection(another)  within a Collection
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/intersection'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_parent_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_parent_get

        Get the list of zones parents of a given zone  within a Collection
        """
        query_string = [('inherit_id', false),
                        ('levels', 1),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/parent'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example', zonal_id='zonal_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_sibling_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_sibling_get

        Get the list of zones siblings of a given zone  within a Collection
        """
        query_string = [('inherit_id', false),
                        ('levels', 1),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/sibling'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example', zonal_id='zonal_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_sym_difference_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_sym_difference_get

        Get the list of zonalID that are the result of zoneId.symDifference(another)  within a Collection
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/symDifference'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_dggs_dggs_rsid_zone_zonal_id_union_get(self):
        """Test case for collections_collection_id_dggs_dggs_rsid_zone_zonal_id_union_get

        Get the list of zonalID that are the result of zoneId.union(another)  within a Collection
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('range_refine', 56),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/collections/{collectionId}/dggs/{dggsRSID}/zone/{ZonalID}/union'.format(collection_id='collection_id_example', dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
