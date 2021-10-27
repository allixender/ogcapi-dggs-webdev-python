import connexion
import six


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
from dggs_api_server import util

from dggs_api_server.models.collections import Collections  # noqa: E501
from dggs_api_server.models.link import Link  # noqa: E501
from dggs_api_server.models.keyword import Keyword  # noqa: E501
from dggs_api_server.models.collection_list import CollectionList  # noqa: E501

from dggs_api_server.models.conf_classes import ConfClasses  # noqa: E501

from dggs_api_server.models.exception import DggsException  # noqa: E501
from dggs_api_server.models.landing_page import LandingPage  # noqa: E501
from dggs_api_server.models.spatial_extent import SpatialExtent

from dggs_api_server.dataaccess import dao
from dggs_api_server.controllers import canonical_url_for_path
from flask import redirect, request


def api_get(f=None):  # noqa: E501
    """This Document

    This Document # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: str
    """
    uri = canonical_url_for_path(path="openapi.json")
    return redirect(location=uri, code=301)


def collections_get(f=None):  # noqa: E501
    """the collections in a dataset shared from this server

    A list of all collections available in this dataset. # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: Collections
    """
    c_list = dao.catalog_get()

    collections = []

    for cat_e in c_list:
        keywords = []
        for kw in cat_e["variables"]:
            keywords.append(Keyword(keyword=kw))

        cl = Collections(
            id=cat_e["table_name"],
            title=cat_e["table_name"],
            description=cat_e["description"],
            keywords=keywords,
            attribution="attribution",
            extent=SpatialExtent(bbox=cat_e["extent"], crs="WGS84"),
            crs=cat_e["dggs_type"],
            links=[
                Link(
                    href=cat_e["meta_url"],
                    rel="alternate",
                    type="text/html",
                    title=cat_e["description"],
                )
            ],
        )
        collections.append(cl)

    links = [
        Link(
            {
                "href": canonical_url_for_path(path="/collections.json"),
                "rel": "self",
                "title": "this document",
                "type": "application/json",
            }
        ),
        Link(
            {
                "href": canonical_url_for_path(path="/collections.html"),
                "rel": "alternate",
                "title": "this document as HTML",
                "type": "text/html",
            }
        ),
    ]
    c = CollectionList(links=links, collections=collections)
    return c


def conformance_get(f=None):  # noqa: E501
    """conformance_get

    A list of all requirements classes specified in a standard that the server conforms to. # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: ConfClasses
    """
    d = [
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
        "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    ]
    return ConfClasses(d)


def describe_collection(collection_id, f=None):  # noqa: E501
    """describe a collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param f: The format of the response. If no value is provided, the standard http rules apply, i.e., the accept header is used to determine the format. Pre-defined values are \&quot;json\&quot; and \&quot;html\&quot;. The response to other values is determined by the server.
    :type f: str

    :rtype: Collections
    """
    cat_e = dao.catalog_describe_id_get(collection_id)

    links = [
        Link(href=h, rel="alternate", type="text/html", title=cat_e["description"])
        for h in cat_e["links"]
    ]
    links.append(
        Link(
            {
                "href": canonical_url_for_path(
                    path=f"/collections/{cat_e['table_name']}.json"
                ),
                "rel": "self",
                "title": "this document",
                "type": "application/json",
            }
        )
    )
    links.append(
        Link(
            {
                "href": canonical_url_for_path(
                    path=f"/collections/{cat_e['table_name']}.html"
                ),
                "rel": "alternate",
                "title": "this document as HTML",
                "type": "text/html",
            }
        )
    )
    keywords = []
    for kw in cat_e["variables"]:
        keywords.append(Keyword(keyword=kw))

    cl = Collections(
        id=cat_e["table_name"],
        title=cat_e["table_name"],
        description=cat_e["description"],
        keywords=keywords,
        attribution="attribution",
        extent=SpatialExtent(bbox=cat_e["extent"], crs="WGS84"),
        crs=cat_e["dggs_type"],
        links=[
            Link(
                href=cat_e["meta_url"],
                rel="alternate",
                type="text/html",
                title=cat_e["description"],
            )
        ],
    )

    return cl


def root_get(f=None):  # noqa: E501
    """landing page

    The landing page provides links to the API definition, the conformance statements and to the feature collections in this dataset. # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: LandingPage
    """
    lp_dict = {
        "description": "Access to data about Estonia via a Web API that aims to conform to the OGC API DGGS specification.",
        "links": [
            {
                "href": canonical_url_for_path(),
                "rel": "self",
                "title": "this document",
                "type": "application/json",
            },
            {
                "href": canonical_url_for_path(path="openapi.json"),
                "rel": "service-desc",
                "title": "the API definition",
                "type": "application/vnd.oai.openapi+json;version=3.0",
            },
            {
                "href": canonical_url_for_path(path="ui"),
                "rel": "service-doc",
                "title": "the API documentation",
                "type": "text/html",
            },
            {
                "href": canonical_url_for_path(path="conformance"),
                "rel": "conformance",
                "title": "OGC API conformance classes implemented by this server",
                "type": "application/json",
            },
            {
                "href": canonical_url_for_path(path="collections"),
                "rel": "data",
                "title": "Information about the feature collections",
                "type": "application/json",
            },
        ],
        "title": "DGGS coded data in Estonia",
    }
    return LandingPage(lp_dict)
