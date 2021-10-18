# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.distance import Distance  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZoneQueryOpsController(BaseTestCase):
    """ZoneQueryOpsController integration test stubs"""

    def test_collections_collection_id_zone_zone_id_distance_get(self):
        """Test case for collections_collection_id_zone_zone_id_distance_get

        Test if the current ZoneId is withinDistance another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/rggibb/dggs-zonequery/0.0.4/collections/{collectionId}/zone/{zoneId}/distance'.format(collection_id='collection_id_example', zone_id='zone_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
