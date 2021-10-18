import connexion
import six

from swagger_server.models.distance import Distance  # noqa: E501
from swagger_server.models.exception import Exception  # noqa: E501
from swagger_server import util


def collections_collection_id_zone_zone_id_distance_get(collection_id, zone_id, zonal_id, project_to=None):  # noqa: E501
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
    return 'do some magic!'
