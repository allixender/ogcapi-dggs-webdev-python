import connexion
import six

import connexion
import six

from dggs_api_server.models.distance import Distance  # noqa: E501

from dggs_api_server.models.collection import Collection  # noqa: E501
from dggs_api_server.models.exception import (
    DggsException,
    DggsCollectionIdNotFoundError,
)  # noqa: E501
from dggs_api_server.models.zone_collection_geo_json import (
    ZoneCollectionGeoJSON,
)  # noqa: E501
from dggs_api_server.models.zone_geo_json import ZoneGeoJSON  # noqa: E501
from dggs_api_server import util

# from dggs_api_server.dataaccess.clickhouse_dao import db, dggs_access_collections_collection_id_describe_get
from dggs_api_server.dataaccess import dao


def collections_collection_id_describe_get(collection_id):  # noqa: E501
    """Describes a particular DGGS

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str

    :rtype: Collection
    """

    rs = dao.dggs_access_collections_collection_id_describe_get(collection_id)

    if not rs is None:
        return rs
    else:
        return DggsCollectionIdNotFoundError()


def collections_collection_id_zone_get(collection_id):  # noqa: E501
    """Access the definition of a particular zone

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str

    :rtype: ZoneGeoJSON
    """
    if collection_id in ["TB16-Pix"]:
        d = {}
        return ZoneGeoJSON(d)
        # return 'do some magic!'
    else:
        return DggsCollectionIdNotFoundError()


def collections_collection_id_zone_zone_id_buffer_get(
    collection_id, zone_id, distance=None, project_to=None
):  # noqa: E501
    """Get the list of zones children of a given zone (should it return just a list of identifiers instead of a GeoJSON collection?)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param distance:
    :type distance: float
    :param project_to:
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    if collection_id in ["TB16-Pix"]:
        d = {}
        return ZoneCollectionGeoJSON(d)
        # return 'do some magic!'
    else:
        return DggsCollectionIdNotFoundError()


def collections_collection_id_zone_zone_id_child_get(
    collection_id, zone_id, inherit_id=None, levels=None
):  # noqa: E501
    """Get the list of zones children of a given zone (should it return just a list of identifiers instead of a GeoJSON collection?)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param inherit_id:
    :type inherit_id: bool
    :param levels:
    :type levels: int

    :rtype: ZoneCollectionGeoJSON
    """
    if collection_id in ["TB16-Pix"]:
        d = {}
        return ZoneCollectionGeoJSON(d)
        # return 'do some magic!'
    else:
        return DggsCollectionIdNotFoundError()


def collections_collection_id_zone_zone_id_child_of_get(
    collection_id, zone_id, zonal_id, inherit_id=None, project_to=None
):  # noqa: E501
    """Determine if the another ZonalID is a childOf the input ZonaID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param zonal_id:
    :type zonal_id: str
    :param inherit_id:
    :type inherit_id: bool
    :param project_to:
    :type project_to: List[str]

    :rtype: bool
    """
    if collection_id in ["TB16-Pix"]:
        d = {}
        return True
        # return 'do some magic!'
    else:
        return DggsCollectionIdNotFoundError()


def collections_collection_id_zone_zone_id_intersects_get(
    collection_id, zone_id, zonal_id, project_to=None
):  # noqa: E501
    """Determine if the another ZonalID intersects with the ZonaID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param zonal_id:
    :type zonal_id: str
    :param project_to:
    :type project_to: List[str]

    :rtype: bool
    """
    return "do some magic!"


def collections_collection_id_zone_zone_id_overlaps_get(
    collection_id, zone_id, zonal_id, project_to=None
):  # noqa: E501
    """Determine if the another ZonalID overlaps with the ZonaID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param zonal_id:
    :type zonal_id: str
    :param project_to:
    :type project_to: List[str]

    :rtype: bool
    """
    return "do some magic!"


def collections_collection_id_zone_zone_id_parent_of_get(
    collection_id, zone_id, zonal_id, inherit_id=None, project_to=None
):  # noqa: E501
    """Determine if the another ZonalID is a parentOf the input ZonaID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param zonal_id:
    :type zonal_id: str
    :param inherit_id:
    :type inherit_id: bool
    :param project_to:
    :type project_to: List[str]

    :rtype: bool
    """
    return "do some magic!"


def collections_collection_id_zone_zone_id_sibling_of_get(
    collection_id, zone_id, zonal_id, inherit_id=None, project_to=None
):  # noqa: E501
    """Determine if the another ZonalID is a siblingOf the input ZonaID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param zonal_id:
    :type zonal_id: str
    :param inherit_id:
    :type inherit_id: bool
    :param project_to:
    :type project_to: List[str]

    :rtype: bool
    """
    return "do some magic!"


def collections_collection_id_zones_get(
    collection_id, resolution, bbox=None, zone_id_list=None, limit=None
):  # noqa: E501
    """Access the list of zones in a given DGGS. Can list either all the zones, or a particular subset based on resolution, WGS84 bbox, or list of containing zones (e.g., polygon defined in DGGS terms)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param resolution:
    :type resolution: float
    :param bbox: Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Minimum value, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Maximum value, coordinate axis 3 (optional)  The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter &#x60;bbox-crs&#x60;.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box.  If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries.
    :type bbox: List[float]
    :param zone_id_list: Comma separated list of zone identifiers
    :type zone_id_list: List[str]
    :param limit: The optional limit parameter limits the number of items that are presented in the response document.  Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted.  Minimum &#x3D; 1. Maximum &#x3D; 10000. Default &#x3D; 10.
    :type limit: int

    :rtype: ZoneCollectionGeoJSON
    """
    return "do some magic!"


def collections_collection_id_zone_zone_id_distance_get(
    collection_id, zone_id, zonal_id, project_to=None
):  # noqa: E501
    """Test if the current ZoneId is withinDistance another ZonalID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id:
    :type zone_id: str
    :param zonal_id:
    :type zonal_id: str
    :param project_to:
    :type project_to: List[str]

    :rtype: Distance
    """
    return "do some magic!"
