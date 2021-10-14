import connexion
import six

from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server.models.relative_position import RelativePosition  # noqa: E501
from swagger_server import util


def collections_collection_id_zone_zone_id_relate_get(collection_id, zone_id, zonal_id, matrix=None, project_to=None):  # noqa: E501
    """Test if the current ZoneId satisfies relate matrix another ZonalID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param matrix: 
    :type matrix: List[str]
    :param project_to: 
    :type project_to: List[str]

    :rtype: bool
    """
    return 'do some magic!'


def collections_collection_id_zone_zone_id_relate_position_get(collection_id, zone_id, zonal_id, relate=None, project_to=None):  # noqa: E501
    """Test if the current ZoneId satisfies relatePosition relativePosition another ZonalID

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param zone_id: 
    :type zone_id: str
    :param zonal_id: 
    :type zonal_id: str
    :param relate: 
    :type relate: dict | bytes
    :param project_to: 
    :type project_to: List[str]

    :rtype: bool
    """
    if connexion.request.is_json:
        relate = RelativePosition.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
