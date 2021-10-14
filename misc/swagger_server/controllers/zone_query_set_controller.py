import connexion
import six

from swagger_server.models.distance import Distance  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.zone_collection_geo_json import ZoneCollectionGeoJSON  # noqa: E501
from swagger_server import util


def collections_collection_id_zone_zone_id_buffer_get(collection_id, zone_id, dist=None, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalId that are within a buffer of dist from the given zoneId

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param dist: 
    :type dist: dict | bytes
    :param range_refine: 
    :type range_refine: List[int]
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    if connexion.request.is_json:
        dist = Distance.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def collections_collection_id_zone_zone_id_child_get(collection_id, zone_id, inherit_id=None, levels=None, project_to=None):  # noqa: E501
    """Get the list of zones children of a given zone

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param inherit_id: 
    :type inherit_id: bool
    :param levels: 
    :type levels: int
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_difference_get(collection_id, zone_id, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.difference(another)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param range_refine: 
    :type range_refine: List[int]
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_intersection_get(collection_id, zone_id, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.intersection(another)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param range_refine: 
    :type range_refine: List[int]
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_parent_get(collection_id, zone_id, inherit_id=None, levels=None, project_to=None):  # noqa: E501
    """Get the list of zones parents of a given zone

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param inherit_id: 
    :type inherit_id: bool
    :param levels: 
    :type levels: int
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_sibling_get(collection_id, zone_id, inherit_id=None, levels=None, project_to=None):  # noqa: E501
    """Get the list of zones siblings of a given zone

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param inherit_id: 
    :type inherit_id: bool
    :param levels: 
    :type levels: int
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_sym_difference_get(collection_id, zone_id, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.symDifference(another)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param range_refine: 
    :type range_refine: List[int]
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_union_get(collection_id, zone_id, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.union(another)

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param range_refine: 
    :type range_refine: List[int]
    :param project_to: 
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'
