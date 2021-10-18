try:
    from h3 import h3
except ImportError:
    print("H3 library not available")


def get_parent(cell_id):
    parent = h3.h3_to_parent(cell_id)
    return parent


def fill_area(area_json, resolution):
    hexagons = h3.polyfill(area_json, resolution)
    return hexagons
