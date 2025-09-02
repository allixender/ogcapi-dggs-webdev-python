import connexion
import six

from dggs_api_server.models.distance import Distance  # noqa: E501
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


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_distance_get(collection_id, dggs_rsid, zonal_id, project_to=None):  # noqa: E501
    """Test if the current ZoneId is withinDistance another ZonalID within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: type ZonalIdentifier, mandatory. Specifies the target region for the query. In zonal query a zone’s identifier provides sufficient description of its topology. ZonalIdentifier therefore takes the place of the geometry data used in Query2D and Query3D for both the source and the target.
    :type zonal_id: str
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: Distance
    """
    return 'do some magic!'
