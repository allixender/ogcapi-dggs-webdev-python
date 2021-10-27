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
from dggs_api_server.controllers import absolute_url_from_path


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
