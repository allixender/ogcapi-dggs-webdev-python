"""
/ [get]: dggs_api_server.controllers.capabilities_controller
/conformance [get]: dggs_api_server.controllers.capabilities_controller
/collections [get]: dggs_api_server.controllers.capabilities_controller

/collections/{collectionId}/describe [get]: dggs_api_server.controllers.dggs_access_controller
/collections/{collectionId}/zones [get]: dggs_api_server.controllers.dggs_access_controller
/collections/{collectionId}/zone [get]: dggs_api_server.controllers.dggs_access_controller

/collections/{collectionId}/zone/{zoneId}/distance [get]: dggs_api_server.controllers.zone_query_ops_controller

/collections/{collectionId}/zone/{zoneId}/buffer [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/difference [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/intersection [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/symDifference [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/union [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/child [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/parent [get]: dggs_api_server.controllers.zone_query_set_controller
/collections/{collectionId}/zone/{zoneId}/sibling [get]: dggs_api_server.controllers.zone_query_set_controller

/collections/{collectionId}/zone/{zoneId}/relativePosition [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/contains [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/crosses [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/disjoint [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/equals [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/intersects [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/overlaps [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/touches [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/within [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/withinDistance [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/childOf [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/parentOf [get]: dggs_api_server.controllers.zone_query_query_controller
/collections/{collectionId}/zone/{zoneId}/siblingOf [get]: dggs_api_server.controllers.zone_query_query_controller

/collections/{collectionId}/zone/{zoneId}/relate [get]: dggs_api_server.controllers.zone_query_reference_controller
/collections/{collectionId}/zone/{zoneId}/relatePosition [get]: dggs_api_server.controllers.zone_query_reference_controller
"""
