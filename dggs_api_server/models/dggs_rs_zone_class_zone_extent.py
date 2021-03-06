# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server.models.dggs_rs_zone_class_zone_extent_zone_error_budget import DggsRsZoneClassZoneExtentZoneErrorBudget  # noqa: F401,E501
from dggs_api_server import util


class DggsRsZoneClassZoneExtent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, spatial_units: str=None, median_spatial_extent: float=None, temporal_units: str=None, temporal_extent: float=None, zone_error_budget: DggsRsZoneClassZoneExtentZoneErrorBudget=None):  # noqa: E501
        """DggsRsZoneClassZoneExtent - a model defined in Swagger

        :param spatial_units: The spatial_units of this DggsRsZoneClassZoneExtent.  # noqa: E501
        :type spatial_units: str
        :param median_spatial_extent: The median_spatial_extent of this DggsRsZoneClassZoneExtent.  # noqa: E501
        :type median_spatial_extent: float
        :param temporal_units: The temporal_units of this DggsRsZoneClassZoneExtent.  # noqa: E501
        :type temporal_units: str
        :param temporal_extent: The temporal_extent of this DggsRsZoneClassZoneExtent.  # noqa: E501
        :type temporal_extent: float
        :param zone_error_budget: The zone_error_budget of this DggsRsZoneClassZoneExtent.  # noqa: E501
        :type zone_error_budget: DggsRsZoneClassZoneExtentZoneErrorBudget
        """
        self.swagger_types = {
            'spatial_units': str,
            'median_spatial_extent': float,
            'temporal_units': str,
            'temporal_extent': float,
            'zone_error_budget': DggsRsZoneClassZoneExtentZoneErrorBudget
        }

        self.attribute_map = {
            'spatial_units': 'spatialUnits',
            'median_spatial_extent': 'medianSpatialExtent',
            'temporal_units': 'temporalUnits',
            'temporal_extent': 'temporalExtent',
            'zone_error_budget': 'zoneErrorBudget'
        }
        self._spatial_units = spatial_units
        self._median_spatial_extent = median_spatial_extent
        self._temporal_units = temporal_units
        self._temporal_extent = temporal_extent
        self._zone_error_budget = zone_error_budget

    @classmethod
    def from_dict(cls, dikt) -> 'DggsRsZoneClassZoneExtent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The dggsRsZoneClass_zoneExtent of this DggsRsZoneClassZoneExtent.  # noqa: E501
        :rtype: DggsRsZoneClassZoneExtent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def spatial_units(self) -> str:
        """Gets the spatial_units of this DggsRsZoneClassZoneExtent.

        Units to define the spatial extent  # noqa: E501

        :return: The spatial_units of this DggsRsZoneClassZoneExtent.
        :rtype: str
        """
        return self._spatial_units

    @spatial_units.setter
    def spatial_units(self, spatial_units: str):
        """Sets the spatial_units of this DggsRsZoneClassZoneExtent.

        Units to define the spatial extent  # noqa: E501

        :param spatial_units: The spatial_units of this DggsRsZoneClassZoneExtent.
        :type spatial_units: str
        """

        self._spatial_units = spatial_units

    @property
    def median_spatial_extent(self) -> float:
        """Gets the median_spatial_extent of this DggsRsZoneClassZoneExtent.

        Spatial Extent  # noqa: E501

        :return: The median_spatial_extent of this DggsRsZoneClassZoneExtent.
        :rtype: float
        """
        return self._median_spatial_extent

    @median_spatial_extent.setter
    def median_spatial_extent(self, median_spatial_extent: float):
        """Sets the median_spatial_extent of this DggsRsZoneClassZoneExtent.

        Spatial Extent  # noqa: E501

        :param median_spatial_extent: The median_spatial_extent of this DggsRsZoneClassZoneExtent.
        :type median_spatial_extent: float
        """

        self._median_spatial_extent = median_spatial_extent

    @property
    def temporal_units(self) -> str:
        """Gets the temporal_units of this DggsRsZoneClassZoneExtent.

        Units to define the temporal extent  # noqa: E501

        :return: The temporal_units of this DggsRsZoneClassZoneExtent.
        :rtype: str
        """
        return self._temporal_units

    @temporal_units.setter
    def temporal_units(self, temporal_units: str):
        """Sets the temporal_units of this DggsRsZoneClassZoneExtent.

        Units to define the temporal extent  # noqa: E501

        :param temporal_units: The temporal_units of this DggsRsZoneClassZoneExtent.
        :type temporal_units: str
        """

        self._temporal_units = temporal_units

    @property
    def temporal_extent(self) -> float:
        """Gets the temporal_extent of this DggsRsZoneClassZoneExtent.

        Temporal Extent  # noqa: E501

        :return: The temporal_extent of this DggsRsZoneClassZoneExtent.
        :rtype: float
        """
        return self._temporal_extent

    @temporal_extent.setter
    def temporal_extent(self, temporal_extent: float):
        """Sets the temporal_extent of this DggsRsZoneClassZoneExtent.

        Temporal Extent  # noqa: E501

        :param temporal_extent: The temporal_extent of this DggsRsZoneClassZoneExtent.
        :type temporal_extent: float
        """

        self._temporal_extent = temporal_extent

    @property
    def zone_error_budget(self) -> DggsRsZoneClassZoneExtentZoneErrorBudget:
        """Gets the zone_error_budget of this DggsRsZoneClassZoneExtent.


        :return: The zone_error_budget of this DggsRsZoneClassZoneExtent.
        :rtype: DggsRsZoneClassZoneExtentZoneErrorBudget
        """
        return self._zone_error_budget

    @zone_error_budget.setter
    def zone_error_budget(self, zone_error_budget: DggsRsZoneClassZoneExtentZoneErrorBudget):
        """Sets the zone_error_budget of this DggsRsZoneClassZoneExtent.


        :param zone_error_budget: The zone_error_budget of this DggsRsZoneClassZoneExtent.
        :type zone_error_budget: DggsRsZoneClassZoneExtentZoneErrorBudget
        """

        self._zone_error_budget = zone_error_budget
