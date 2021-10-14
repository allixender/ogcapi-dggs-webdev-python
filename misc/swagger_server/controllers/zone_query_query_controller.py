import connexion
import six

from swagger_server.models.distance import Distance  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.relative_position import RelativePosition  # noqa: E501
from swagger_server import util


def collections_collection_id_zone_zone_id_child_of_get(collection_id, zone_id, zonal_id, inherit_id=None, project_to=None):  # noqa: E501
    """Test if the current ZoneId is childOf another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_contains_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId contains another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_crosses_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId crosses another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_disjoint_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId is disjoint another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_equals_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId equals another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_intersects_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId intersects another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_overlaps_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId overlaps another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_parent_of_get(collection_id, zone_id, zonal_id, inherit_id=None, project_to=None):  # noqa: E501
    """Test if the current ZoneId is parentOf another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_relative_position_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Determine the relativePosition of another ZonalID to the current ZoneId

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param project_to: 
    :type project_to: List[str]

    :rtype: RelativePosition
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_sibling_of_get(collection_id, zone_id, zonal_id, inherit_id=None, project_to=None):  # noqa: E501
    """Test if the current ZoneId is siblingOf another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_touches_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId touches another ZonalID

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
    return 'do some magic!'


def collections_collection_id_zone_zone_id_within_distance_get(collection_id, zone_id, zonal_id, dist=None, project_to=None):  # noqa: E501
    """Test if the current ZoneId is withinDistance another ZonalID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param dist: 
    :type dist: dict | bytes
    :param project_to: 
    :type project_to: List[str]

    :rtype: bool
    """
    if connexion.request.is_json:
        dist = Distance.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def collections_collection_id_zone_zone_id_within_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId within another ZonalID

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
    return 'do some magic!'
