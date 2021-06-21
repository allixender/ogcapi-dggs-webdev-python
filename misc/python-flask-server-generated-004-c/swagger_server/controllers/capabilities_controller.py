import connexion
import six

from swagger_server.models.collection_list import CollectionList  # noqa: E501
from swagger_server.models.conf_classes import ConfClasses  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.landing_page import LandingPage  # noqa: E501
from swagger_server import util


def collections_get():  # noqa: E501
    """the list of supported collections

     # noqa: E501


    :rtype: CollectionList
    """
    return 'do some magic!'


def conformance_get():  # noqa: E501
    """information about specifications that this API conforms to (we may not need one)

    A list of all conformance classes specified in a standard that the server conforms to. # noqa: E501


    :rtype: ConfClasses
    """
    return 'do some magic!'


def root_get():  # noqa: E501
    """landing page

    The landing page provides links to the API definition, the conformance statements and to other resources provided by the API. # noqa: E501


    :rtype: LandingPage
    """
    return 'do some magic!'
