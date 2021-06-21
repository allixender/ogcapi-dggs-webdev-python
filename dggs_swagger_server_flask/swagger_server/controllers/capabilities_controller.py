import connexion
import six

from swagger_server.models.collection_list import CollectionList  # noqa: E501
from swagger_server.models.conf_classes import ConfClasses  # noqa: E501
from swagger_server.models.exception import DggsException  # noqa: E501
from swagger_server.models.landing_page import LandingPage  # noqa: E501
from swagger_server import util

from swagger_server.models.collection_list import CollectionList  # noqa: E501
from swagger_server.models.conf_classes import ConfClasses

def collections_get():  # noqa: E501
    """the list of supported collections

     # noqa: E501


    :rtype: CollectionList
    """
    d = {
  "dggs-list": [
    {
      "description": "The rHealPix DGGS",
      "id": "TB16-Pix",
      "links": [
        {
          "href": "https://iopscience.iop.org/article/10.1088/1755-1315/34/1/012012/pdf",
          "rel": "describedBy",
          "title": "The rHealPix DGGS specification",
          "type": "application/PDF"
        },
        {
          "href": "http://data.example.org/dggs/rHealPix/zones",
          "rel": "zones",
          "type": "appplication/json"
        }
      ],
      "resolutions": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "title": "The Testbed16 DGGS based on rHealPix"
    },
    {
      "description": "The H3 DGGS",
      "id": "H3",
      "links": [
        {
          "href": "https://eng.uber.com/h3/",
          "rel": "describedBy",
          "title": "The H3 specification",
          "type": "text/html"
        },
        {
          "href": "http://data.example.org/dggs/H3/zones",
          "rel": "zones",
          "type": "appplication/json"
        }
      ],
      "resolutions": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16
      ],
      "title": "H3"
    }
  ],
  "links": [
    {
      "href": "http://data.example.org/dggs.json",
      "rel": "self",
      "title": "this document",
      "type": "application/json"
    },
    {
      "href": "http://data.example.org/dggs.html",
      "rel": "alternate",
      "title": "this document as HTML",
      "type": "text/html"
    }
  ]
}
    return CollectionList(d)


def conformance_get():  # noqa: E501
    """information about specifications that this API conforms to (we may not need one)

    A list of all conformance classes specified in a standard that the server conforms to. # noqa: E501


    :rtype: ConfClasses
    """
    d = {
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson"
  ]
}
    return ConfClasses(d)


def root_get():  # noqa: E501
    """landing page

    The landing page provides links to the API definition, the conformance statements and to other resources provided by the API. # noqa: E501


    :rtype: LandingPage
    """
    # return 'do some magic!'
    lp_dict = {
  "description": "Access to data about buildings in the city of Bonn via a Web API that conforms to the OGC API Features specification.",
  "links": [
    {
      "href": "http://data.example.org/",
      "rel": "self",
      "title": "this document",
      "type": "application/json"
    },
    {
      "href": "http://data.example.org/api",
      "rel": "service-desc",
      "title": "the API definition",
      "type": "application/vnd.oai.openapi+json;version=3.0"
    },
    {
      "href": "http://data.example.org/api.html",
      "rel": "service-doc",
      "title": "the API documentation",
      "type": "text/html"
    },
    {
      "href": "http://data.example.org/conformance",
      "rel": "conformance",
      "title": "OGC API conformance classes implemented by this server",
      "type": "application/json"
    },
    {
      "href": "http://data.example.org/collections",
      "rel": "data",
      "title": "Information about the feature collections",
      "type": "application/json"
    }
  ],
  "title": "Buildings in Bonn"
}
    return LandingPage(lp_dict)
