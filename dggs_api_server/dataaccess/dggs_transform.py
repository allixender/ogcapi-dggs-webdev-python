from dggs_api_server.models.exception import (
    DggsException,
    DggsTypeNotSupportedError,
)  # noqa: E501

from dggs_api_server.dataaccess import h3_transform

try:
    # import rhealpixdggs as rhpix
    # import rhealpixdggs.dggs as rhpix_dggs
    from dggs_api_server.dataaccess import rhpix_transform
except ImportError:
    print("RHEALPIX library not available")


def get_dggs_base_info(dggs_type, catalog_dict):
    if dggs_type == "H3":
        return h3_transform.get_dggs_base_info(catalog_dict)
    elif dggs_type == "RHEALPIX":
        return rhpix_transform.get_dggs_base_info(catalog_dict)
    else:
        return DggsTypeNotSupportedError()


def get_parent(dggs_type, cell_id):
    if dggs_type == "H3":
        return h3_transform.get_parent(cell_id)
    elif dggs_type == "RHEALPIX":
        return rhpix_transform.get_parent(cell_id)
    else:
        return DggsTypeNotSupportedError()


def get_parents_max_list(dggs_type, zone_id_list, max_num):
    if dggs_type == "H3":
        return h3_transform.get_parents_max_list(zone_id_list, max_num)
    elif dggs_type == "RHEALPIX":
        return rhpix_transform.get_parents_max_list(zone_id_list, max_num)
    else:
        return DggsTypeNotSupportedError()


def fill_area(dggs_type, area_json, resolution):
    if dggs_type == "H3":
        return h3_transform.fill_area(area_json, resolution)
    elif dggs_type == "RHEALPIX":
        return rhpix_transform.fill_area(area_json, resolution)
    else:
        return DggsTypeNotSupportedError()
