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

from dggs_api_server.models.dggs_list import DggsList  # noqa: E501
from dggs_api_server.models.dggs_rs_parameters import DggsRsParameters  # noqa: E501
from dggs_api_server.models.zone_collection_geo_json import (
    ZoneCollectionGeoJSON,
)  # noqa: E501
from dggs_api_server.models.zone_geo_json import ZoneGeoJSON  # noqa: E501
from dggs_api_server import util


from dggs_api_server.models.collections import Collections  # noqa: E501
from dggs_api_server.models.exception import (
    DggsException,
    DggsCollectionIdNotFoundError,
)  # noqa: E501

# from dggs_api_server.dataaccess.clickhouse_dao import db, dggs_access_collections_collection_id_describe_get
from dggs_api_server.dataaccess import dao
from dggs_api_server.controllers import canonical_url_for_path
from flask import redirect, request


def dggs_dggs_rsid_zone_zonal_idget(dggs_rsid, zonal_id):  # noqa: E501
    """Access the definition of a particular zone

     # noqa: E501

    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id:
    :type zonal_id: str

    :rtype: ZoneGeoJSON
    """
    rs = dao.dggs_access_collections_collection_id_zone_get(dggs_rsid, zonal_id)

    if not rs is None:
        return rs
    else:
        return DggsCollectionIdNotFoundError()


def dggs_dggs_rsid_zones_get(
    dggs_rsid, f=None, bbox=None, range_refine=None, offset=None, limit=None
):  # noqa: E501
    """Access the list of zones in a given DGGS. Can list either all the zones, or a particular subset based on resolution, WGS84 bbox, or list of containing zones (e.g., polygon defined in DGGS terms)

     # noqa: E501

    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str
    :param bbox: Only features that have a geometry that intersects the bounding box are selected.     The bounding box is provided as four or six numbers, depending on whether the     coordinate reference system includes a vertical axis (height or depth):  * Lower left corner, coordinate axis 1     * Lower left corner, coordinate axis 2     * Minimum value, coordinate axis 3 (optional)     * Upper right corner, coordinate axis 1     * Upper right corner, coordinate axis 2     * Maximum value, coordinate axis 3 (optional)  The coordinate reference system of the values is WGS 84 longitude/latitude     (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate     reference system is specified in the parameter &#x60;bbox-crs&#x60;.  For WGS 84 longitude/latitude the values are in most cases the sequence of     minimum longitude, minimum latitude, maximum longitude and maximum latitude.     However, in cases where the box spans the antimeridian the first value     (west-most box edge) is larger than the third value (east-most box edge). If the vertical axis is included, the third and the sixth number are     the bottom and the top of the 3-dimensional bounding box.  If a feature has multiple spatial geometry properties, it is the decision of the     server whether only a single spatial geometry property is used to determine     the extent or all relevant geometries.
    :type bbox: List[float]
    :param range_refine: Specifies the range of refinement levels to include in the return «set». The lower and upper bounds in the refinementLevelRange datatype are both included in the range.
    :type range_refine: List[int]
    :param offset: The optional offset parameter specifies the number of items of a collection to skip before constructing the resultset to be returned in the response document. Minimum &#x3D; 0, Maximum &#x3D; 9999, Default &#x3D; 10
    :type offset: int
    :param limit: The optional limit parameter limits the number of items that are presented in the response document. Only items are counted that are on the first level of the collection in the response document.     Nested objects contained within the explicitly requested items shall not be counted. Minimum &#x3D; 1. Maximum &#x3D; 10000. Default &#x3D; 10.
    :type limit: int

    :rtype: ZoneCollectionGeoJSON
    """
    resolution = range_refine[0] if range_refine is not None else None

    rs = dao.dggs_access_collections_collection_id_zones_get(
        dggs_rsid, resolution, bbox=bbox, zone_id_list=None, limit=limit
    )
    if not rs is None:
        return rs
    else:
        return DggsCollectionIdNotFoundError()


def dggs_dggs_rsidget(dggs_rsid, f=None, geometry_stats=None):  # noqa: E501
    """Structural definition and links to OGC API Resources implemented on this server for the selected DGGS Reference System.

     # noqa: E501

    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str
    :param geometry_stats: get full DGGS_RS class statistics e.g. [min,max,mean,median,sd]
    :type geometry_stats: List[str]

    :rtype: DggsRsParameters
    """
    return "do some magic!"


def dggs_get(f=None):  # noqa: E501
    """List of DGGS Resource Instances

     # noqa: E501

    :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is JSON.
    :type f: str

    :rtype: DggsList
    """
    return "do some magic!"
