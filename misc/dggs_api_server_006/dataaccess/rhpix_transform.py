try:
    import rhealpixdggs as rhpix
    import rhealpixdggs.dggs as rhpix_dggs
except ImportError:
    print("RHEALIX library not available")

import itertools


def get_rhpix_geoid():
    rhpix_geoid = rhpix_dggs.WGS84_003
    return rhpix_geoid


default_rhpix_geoid = get_rhpix_geoid()


def rhpix_suid_to_string(suid):
    return "".join(map(lambda x: str(x), suid))


def rhpix_string_to_suid(s):
    b = s[0]
    rs = map(lambda x: int(x), s[1:])
    suid_chain = (b, *rs)
    return tuple(suid_chain)


def rhpix_cell_id_to_boundary(cell_id, rhpix_geoid=default_rhpix_geoid):
    cell_suid = rhpix_string_to_suid(cell_id)
    c = rhpix_geoid.cell(suid=cell_suid)
    vx = c.vertices(plane=False)
    vx.append(vx[0])
    return vx


def get_parent(cell_id):
    return cell_id[:-1]


def get_parents_max_list(zone_id_list, max_num):
    parent_ids = set(map(lambda cell_id: get_parent(cell_id), zone_id_list))
    if len(parent_ids) > max_num:
        return get_parents_max_list(parent_ids, max_num)
    else:
        return parent_ids


def get_outermost_from_poly(area_json):
    geom_ext = area_json["coordinates"][0]
    y = [p[0] for p in geom_ext]
    x = [p[1] for p in geom_ext]
    ul = (float(min(x)), float(max(y)))
    dr = (float(max(x)), float(min(y)))
    return (ul, dr)


def flatten_cell_list(cell_grid):
    flat_list = []
    for row in cell_grid:
        flat_list.append([rhpix_suid_to_string(cell.suid) for cell in row])
    return flat_list


def fill_area(area_json, resolution, rhpix_geoid=default_rhpix_geoid):
    ul, dr = get_outermost_from_poly(area_json)
    # cells_from_region(1, ul, dr, plane=False)
    rhpix_cells = flatten_cell_list(
        rhpix_geoid.cells_from_region(int(resolution), ul, dr, plane=False)
    )
    list_flat = list(itertools.chain(*rhpix_cells))
    return list_flat
