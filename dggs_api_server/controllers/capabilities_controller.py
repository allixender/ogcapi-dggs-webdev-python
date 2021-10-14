import connexion
import six

from dggs_api_server.models.collection_list import CollectionList  # noqa: E501
from dggs_api_server.models.conf_classes import ConfClasses  # noqa: E501
from dggs_api_server.models.exception import DggsException  # noqa: E501
from dggs_api_server.models.landing_page import LandingPage  # noqa: E501
from dggs_api_server import util

from dggs_api_server.dataaccess import dao


def collections_get():  # noqa: E501
    """the list of supported collections

     # noqa: E501

    :rtype: CollectionList
    """

    return dao.capabilities_collections_get()


def conformance_get():  # noqa: E501
    """information about specifications that this API conforms to (we may not need one)

    A list of all conformance classes specified in a standard that the server conforms to. # noqa: E501


    :rtype: ConfClasses
    """
    d = [
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    ]
    return ConfClasses(d)


def root_get():  # noqa: E501
    """landing page

    The landing page provides links to the API definition, the conformance statements and to other resources provided by the API. # noqa: E501


    :rtype: LandingPage
    """
    # return 'do some magic!'
    lp_dict = {
        "description": "Access to data about Estonia via a Web API that conforms to the OGC API DGGS specification.",
        "links": [
            {
                "href": "http://data.example.org/",
                "rel": "self",
                "title": "this document",
                "type": "application/json",
            },
            {
                "href": "http://data.example.org/api",
                "rel": "service-desc",
                "title": "the API definition",
                "type": "application/vnd.oai.openapi+json;version=3.0",
            },
            {
                "href": "http://data.example.org/api.html",
                "rel": "service-doc",
                "title": "the API documentation",
                "type": "text/html",
            },
            {
                "href": "http://data.example.org/conformance",
                "rel": "conformance",
                "title": "OGC API conformance classes implemented by this server",
                "type": "application/json",
            },
            {
                "href": "http://data.example.org/collections",
                "rel": "data",
                "title": "Information about the feature collections",
                "type": "application/json",
            },
        ],
        "title": "Data in Estonia",
    }
    return LandingPage(lp_dict)
