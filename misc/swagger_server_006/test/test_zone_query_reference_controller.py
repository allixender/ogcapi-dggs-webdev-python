# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.relative_position import RelativePosition  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZoneQueryReferenceController(BaseTestCase):
    """ZoneQueryReferenceController integration test stubs"""

    def test_collections_collection_id_zone_zone_id_relate_get(self):
        """Test case for collections_collection_id_zone_zone_id_relate_get

        Test if the current ZoneId satisfies relate matrix another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('matrix', 'matrix_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/relate'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_collections_collection_id_zone_zone_id_relate_position_get(self):
        """Test case for collections_collection_id_zone_zone_id_relate_position_get

        Test if the current ZoneId satisfies relatePosition relativePosition another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('relate', RelativePosition()),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/relatePosition'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
