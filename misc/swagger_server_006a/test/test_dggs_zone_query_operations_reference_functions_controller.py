# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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


class TestDGGSZoneQueryOperationsReferenceFunctionsController(BaseTestCase):
    """DGGSZoneQueryOperationsReferenceFunctionsController integration test stubs"""

    def test_dggs_dggs_rsid_zone_zonal_id_relate_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_relate_get

        Test if the current ZoneId satisfies relate matrix another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('matrix', 'matrix_example'),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/relate'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zone_zonal_id_relate_position_get(self):
        """Test case for dggs_dggs_rsid_zone_zonal_id_relate_position_get

        Test if the current ZoneId satisfies relatePosition relativePosition another ZonalID
        """
        query_string = [('zonal_id', 'zonal_id_example'),
                        ('relate', RelativePosition()),
                        ('project_to', 'project_to_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}/relatePosition'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
