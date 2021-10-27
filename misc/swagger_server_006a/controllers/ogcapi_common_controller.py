import connexion
import six

from dggs_api_server.models.collections import Collections  # noqa: E501
from dggs_api_server.models.conf_classes import ConfClasses  # noqa: E501
from dggs_api_server.models.exception import Exception  # noqa: E501
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
from dggs_api_server.models.landing_page import LandingPage  # noqa: E501
from dggs_api_server import util


def api_get(f=None):  # noqa: E501
    """This Document

    This Document # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: str
    """
    return 'do some magic!'


def collections_get(f=None):  # noqa: E501
    """the collections in a dataset shared from this server

    A list of all collections available in this dataset. # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: Collections
    """
    return 'do some magic!'


def conformance_get(f=None):  # noqa: E501
    """conformance_get

    A list of all requirements classes specified in a standard that the server conforms to. # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: ConfClasses
    """
    return 'do some magic!'


def describe_collection(collection_id, f=None):  # noqa: E501
    """describe a collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param f: The format of the response. If no value is provided, the standard http rules apply, i.e., the accept header is used to determine the format. Pre-defined values are \&quot;json\&quot; and \&quot;html\&quot;. The response to other values is determined by the server.
    :type f: str

    :rtype: Collections
    """
    return 'do some magic!'


def root_get(f=None):  # noqa: E501
    """landing page

    The landing page provides links to the API definition, the conformance statements and to the feature collections in this dataset. # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: LandingPage
    """
    return 'do some magic!'
