# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from dggs_api_server.models.dggs_list import DggsList  # noqa: E501
from dggs_api_server.models.dggs_rs_parameters import DggsRsParameters  # noqa: E501
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
from dggs_api_server.models.zone_geo_json import ZoneGeoJSON  # noqa: E501
from dggs_api_server.test import BaseTestCase


class TestDGGSCoreController(BaseTestCase):
    """DGGSCoreController integration test stubs"""

    def test_dggs_dggs_rsid_zone_zonal_idget(self):
        """Test case for dggs_dggs_rsid_zone_zonal_idget

        Access the definition of a particular zone
        """
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zone/{ZonalID}'.format(dggs_rsid='dggs_rsid_example', zonal_id='zonal_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsid_zones_get(self):
        """Test case for dggs_dggs_rsid_zones_get

        Access the list of zones in a given DGGS. Can list either all the zones, or a particular subset based on resolution, WGS84 bbox, or list of containing zones (e.g., polygon defined in DGGS terms)
        """
        query_string = [('f', 'f_example'),
                        ('bbox', 3.4),
                        ('range_refine', 56),
                        ('offset', 9999),
                        ('limit', 10000)]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}/zones'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_dggs_rsidget(self):
        """Test case for dggs_dggs_rsidget

        Structural definition and links to OGC API Resources implemented on this server for the selected DGGS Reference System.
        """
        query_string = [('f', 'f_example'),
                        ('geometry_stats', 'geometry_stats_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs/{dggsRSID}'.format(dggs_rsid='dggs_rsid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dggs_get(self):
        """Test case for dggs_get

        List of DGGS Resource Instances
        """
        query_string = [('f', 'f_example')]
        response = self.client.open(
            '/apis/geofizzydrink/ogc_api_dggs/0.0.6/dggs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
