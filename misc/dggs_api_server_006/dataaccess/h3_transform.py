try:
    from h3 import h3
except ImportError:
    print("H3 library not available")


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
