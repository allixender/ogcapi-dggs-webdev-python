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
from dggs_api_server.models.zone_collection_geo_json import ZoneCollectionGeoJSON  # noqa: E501
from dggs_api_server import util


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_buffer_get(collection_id, dggs_rsid, zonal_id, dist=None, project_to=None):  # noqa: E501
    """Get the list of zonalId that are within a buffer of dist from the given zoneId within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: 
    :type zonal_id: str
    :param dist: 
    :type dist: dict | bytes
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    if connexion.request.is_json:
        dist = Distance.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_child_get(collection_id, dggs_rsid, zonal_id, inherit_id=None, levels=None, project_to=None):  # noqa: E501
    """Get the list of zones children of a given zone  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: 
    :type zonal_id: str
    :param inherit_id: type Boolean, optional, default ⇐ False When inheritID has a value of True the result «set» only contains cells for which the IDs have shared inheritance, and a value of False indicates that inheritance is ignored.
    :type inherit_id: bool
    :param levels: type Integer, optional, default ⇐ 1 Levels indicates the relative number of levels in the hierarchy to be traversed in assembling the result «set» Figure 15 illustrates the parent, child and sibling suite of functions through examples.
    :type levels: int
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_difference_get(collection_id, dggs_rsid, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.difference(another)  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: type ZonalIdentifier, mandatory. Specifies the target region for the query. In zonal query a zone’s identifier provides sufficient description of its topology. ZonalIdentifier therefore takes the place of the geometry data used in Query2D and Query3D for both the source and the target.
    :type zonal_id: str
    :param range_refine: Specifies the range of refinement levels to include in the return «set». The lower and upper bounds in the refinementLevelRange datatype are both included in the range.
    :type range_refine: List[int]
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_intersection_get(collection_id, dggs_rsid, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.intersection(another)  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: type ZonalIdentifier, mandatory. Specifies the target region for the query. In zonal query a zone’s identifier provides sufficient description of its topology. ZonalIdentifier therefore takes the place of the geometry data used in Query2D and Query3D for both the source and the target.
    :type zonal_id: str
    :param range_refine: Specifies the range of refinement levels to include in the return «set». The lower and upper bounds in the refinementLevelRange datatype are both included in the range.
    :type range_refine: List[int]
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_parent_get(collection_id, dggs_rsid, zonal_id, inherit_id=None, levels=None, project_to=None):  # noqa: E501
    """Get the list of zones parents of a given zone  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: 
    :type zonal_id: str
    :param inherit_id: type Boolean, optional, default ⇐ False When inheritID has a value of True the result «set» only contains cells for which the IDs have shared inheritance, and a value of False indicates that inheritance is ignored.
    :type inherit_id: bool
    :param levels: type Integer, optional, default ⇐ 1 Levels indicates the relative number of levels in the hierarchy to be traversed in assembling the result «set» Figure 15 illustrates the parent, child and sibling suite of functions through examples.
    :type levels: int
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_sibling_get(collection_id, dggs_rsid, zonal_id, inherit_id=None, levels=None, project_to=None):  # noqa: E501
    """Get the list of zones siblings of a given zone  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: 
    :type zonal_id: str
    :param inherit_id: type Boolean, optional, default ⇐ False When inheritID has a value of True the result «set» only contains cells for which the IDs have shared inheritance, and a value of False indicates that inheritance is ignored.
    :type inherit_id: bool
    :param levels: type Integer, optional, default ⇐ 1 Levels indicates the relative number of levels in the hierarchy to be traversed in assembling the result «set» Figure 15 illustrates the parent, child and sibling suite of functions through examples.
    :type levels: int
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_sym_difference_get(collection_id, dggs_rsid, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.symDifference(another)  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: type ZonalIdentifier, mandatory. Specifies the target region for the query. In zonal query a zone’s identifier provides sufficient description of its topology. ZonalIdentifier therefore takes the place of the geometry data used in Query2D and Query3D for both the source and the target.
    :type zonal_id: str
    :param range_refine: Specifies the range of refinement levels to include in the return «set». The lower and upper bounds in the refinementLevelRange datatype are both included in the range.
    :type range_refine: List[int]
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'


def collections_collection_id_dggs_dggs_rsid_zone_zonal_id_union_get(collection_id, dggs_rsid, zonal_id, range_refine=None, project_to=None):  # noqa: E501
    """Get the list of zonalID that are the result of zoneId.union(another)  within a Collection

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str
    :param dggs_rsid: DGGS implementation identifier
    :type dggs_rsid: str
    :param zonal_id: type ZonalIdentifier, mandatory. Specifies the target region for the query. In zonal query a zone’s identifier provides sufficient description of its topology. ZonalIdentifier therefore takes the place of the geometry data used in Query2D and Query3D for both the source and the target.
    :type zonal_id: str
    :param range_refine: Specifies the range of refinement levels to include in the return «set». The lower and upper bounds in the refinementLevelRange datatype are both included in the range.
    :type range_refine: List[int]
    :param project_to: projectTo specifies an optional reference direction, surface or volume for an operation. Allowed values for each direction are 0 and 1, and spatial directions may also have a value of n. projectTo defines a vector whose starting point is inferred as the point with each projectTo direction whose value is 1 set to 0. It takes one of three forms. In its one-dimensional form for specifying a reference direction, one direction has a value of 1. For example (0,0,0,1) projects to the temporal axis, and (0,0,1,0) projects to the vertical axis. In its two-dimensional form for specifying a reference surface, two directions have a value of 1. For example a surface at height n is specified by a projectTo value of (1,1,n,0) representing the vector [ (0,0,n,0), (1,1,n,0) ]. In its three-dimensional form for specifying a reference volume, three directions have a value of 1. For example (1,1,1,0) projects to a spatial volume without reference to time, and (1,1,n,1) projects to a surface spanning all time at height n. Only the one-D\\dimensional form is supported by relativePosition and relatePosition. While this construct could be used to implement more complex spatio-temporal queries, that isn’t the intent of Query2D, and isn’t specified for ZoneQuery either.
    :type project_to: List[str]

    :rtype: ZoneCollectionGeoJSON
    """
    return 'do some magic!'
