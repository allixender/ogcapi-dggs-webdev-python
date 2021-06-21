# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="WIP: OGC API DGGS ZoneQuery - process style",
    author_email="gibbr@landcareresearch.co.nz",
    url="",
    keywords=["Swagger", "WIP: OGC API DGGS ZoneQuery - process style"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    WARNING - This is work-in-progress.  The API is an evolution of https://app.swaggerhub.com/apis/aaime-sh/dggs-process/0.0.3#/DGGS%20access.  Basic ideas: * The same API elements are used for a DGGS-RS service and a DGGS-Data service * In the case of a DGGS-RS service, the collections are the DGGS instances themselves,   and the returned features have no properties other than the geometry and resolution   (e.g., in GeoJSON the properties object will be &#x60;&#x60;null&#x60;&#x60;) * In the case of a DGGS-Data service, the collections are the sample DGGS data (hence, made available in a particular DGGS instance, too), and the returned features have   actual values associated in the &#x60;&#x60;properties&#x60;&#x60; object.  To care for different use cases, three different output formats will be implemented for each endpoint returning cells: * A classic GeoJSON output, with geometry being either the boundary or the center   point of the zone (to be controlled with a request parameter), for usage in classic   GIS tools. The longitudes ill eventually be extended outside of the -180,180   range to allow visualization by tools that cannot deal properly with dateline crossing. * A DGGSJSON output, small variation of the classic GeoJSON where the geometry is   replaced by an array of zone-ids, to be used in both zone oriented and feature oriented   API (e.g., the) * A plain array of DGGS zone ids, for cases where the attributes are not needed and data transfer compactness is paramount.  Questions, discussion topics: * Support for multiple DDGSs, we are using rHealPix and H3, to offer the   clients and DGGS data server at least a DGGS they are not already supporting natively * Is the API going to be sufficiently self describing that the clients   can figure out everything it needs by just walking the API, or will it need specific knowledge contained in an API profile (e.g, a profile for rHeadlPix, one for H3, cosider for example zoneId and how to determine them) * For parametric DDGSs (e.g., rHealPix) do we expose a specific instance as its own DGGS, or somehow expose the full parameters of the DGGS in each resource? * This API follows a process API, where most resources are a process and one needs to know valid values to hit them   CHANGES * 2020-07-02 initial version * 2020-07-23 usage of zones instead of cells everywhere, extending to support also data DGGS servers. * 2021-06-15 addition of definitions for ZoneQuery operations
    """
)
