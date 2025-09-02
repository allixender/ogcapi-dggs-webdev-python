try:
    from h3 import h3
except ImportError:
    print("H3 library not available")


from dggs_api_server.controllers import canonical_url_for_path
from flask import redirect, request


def get_parent(cell_id):
    parent = h3.h3_to_parent(cell_id)
    return parent


def get_parents_max_list(zone_id_list, max_num):
    parent_ids = set(map(lambda cell_id: get_parent(cell_id), zone_id_list))
    if len(parent_ids) > max_num:
        return get_parents_max_list(parent_ids, max_num)
    else:
        return parent_ids


def fill_area(area_json, resolution):
    hexagons = h3.polyfill(area_json, resolution)
    return hexagons


def get_dggs_base_info(catalog_dict):

    dggsRsId = "H3" + ":" + catalog_dict["table_name"]

    dggs_def = {
        "dggsRsDescription": {
            "title": "Uber H3 DGGS",
            "dggsRsId": dggsRsId,
            "source": ["https://eng.uber.com/h3/"],
        },
        "dggsRsStructure": {
            "gridConstraint": ["cellEquidistant"],
            "surfaceInterpolation": "elliptical",
            "zoneGeometry": {
                "spatialDimension": 2,
                "temporalDimension": 0,
                "topologicalDimension": 2,
            },
            "refinementStrategy": ["nestedChildCell", "centredChildCell"],
            "refinementRatio": 7,
        },
        "dggsRsZoneClasses": [
            {
                "numberOfZones": 5882,
                "refinementLevel": 2,
                "zoneErrorBudget": {
                    "spatialErrorBudget": 11000000000,
                    "spatialUnits": "m^2",
                },
                "zoneExtent": {
                    "spatialExtent": 86745854034,
                    "spatialUnits": "m^2",
                },
            },
            {
                "numberOfZones": 691776122,
                "refinementLevel": 8,
                "zoneErrorBudget": {
                    "spatialErrorBudget": 20000,
                    "spatialUnits": "m^2",
                },
                "zoneExtent": {"spatialExtent": 73732, "spatialUnits": "m^2"},
            },
        ],
        "links": {
            "links": [
                {
                    "href": canonical_url_for_path(path=f"/dggs/{dggsRsId}?f=json"),
                    "rel": "self",
                    "title": "The JSON representation of this OGC API DGGS dggsRsId",
                    "type": "application/json",
                },
                {
                    "href": canonical_url_for_path(path=f"/dggs/{dggsRsId}?f=html"),
                    "rel": "alternate",
                    "title": "The HTML representation of this OGC API DGGS dggsRsId.",
                    "type": "text/html",
                },
                {
                    "href": canonical_url_for_path(
                        path=f"/collections/{catalog_dict['table_name']}?f=json"
                    ),
                    "rel": "data",
                    "title": "The JSON endpoint of the collection indexed with this OGC API DGGS dggsRsId",
                    "type": "application/json",
                },
            ]
        },
    }

    return dggs_def
