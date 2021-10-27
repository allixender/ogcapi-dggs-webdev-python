# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server import util


class DggsRsParametersDggsRsStructureZoneGeometry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, spatial_dimension: float=None, temporal_dimension: float=None, topological_dimension: float=None):  # noqa: E501
        """DggsRsParametersDggsRsStructureZoneGeometry - a model defined in Swagger

        :param spatial_dimension: The spatial_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.  # noqa: E501
        :type spatial_dimension: float
        :param temporal_dimension: The temporal_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.  # noqa: E501
        :type temporal_dimension: float
        :param topological_dimension: The topological_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.  # noqa: E501
        :type topological_dimension: float
        """
        self.swagger_types = {
            'spatial_dimension': float,
            'temporal_dimension': float,
            'topological_dimension': float
        }

        self.attribute_map = {
            'spatial_dimension': 'spatialDimension',
            'temporal_dimension': 'temporalDimension',
            'topological_dimension': 'topologicalDimension'
        }
        self._spatial_dimension = spatial_dimension
        self._temporal_dimension = temporal_dimension
        self._topological_dimension = topological_dimension

    @classmethod
    def from_dict(cls, dikt) -> 'DggsRsParametersDggsRsStructureZoneGeometry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The dggsRsParameters_dggsRsStructure_zoneGeometry of this DggsRsParametersDggsRsStructureZoneGeometry.  # noqa: E501
        :rtype: DggsRsParametersDggsRsStructureZoneGeometry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def spatial_dimension(self) -> float:
        """Gets the spatial_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.

        Topological dimension of the spatial geometry component of zones defined by this DGGS.  # noqa: E501

        :return: The spatial_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.
        :rtype: float
        """
        return self._spatial_dimension

    @spatial_dimension.setter
    def spatial_dimension(self, spatial_dimension: float):
        """Sets the spatial_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.

        Topological dimension of the spatial geometry component of zones defined by this DGGS.  # noqa: E501

        :param spatial_dimension: The spatial_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.
        :type spatial_dimension: float
        """

        self._spatial_dimension = spatial_dimension

    @property
    def temporal_dimension(self) -> float:
        """Gets the temporal_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.

        Topological dimension of the temporal geometry component of zones defined by this DGGS (if present).  # noqa: E501

        :return: The temporal_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.
        :rtype: float
        """
        return self._temporal_dimension

    @temporal_dimension.setter
    def temporal_dimension(self, temporal_dimension: float):
        """Sets the temporal_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.

        Topological dimension of the temporal geometry component of zones defined by this DGGS (if present).  # noqa: E501

        :param temporal_dimension: The temporal_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.
        :type temporal_dimension: float
        """

        self._temporal_dimension = temporal_dimension

    @property
    def topological_dimension(self) -> float:
        """Gets the topological_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.

        Sum of dimensions of topological primitives of zones defined by this DGGS.  # noqa: E501

        :return: The topological_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.
        :rtype: float
        """
        return self._topological_dimension

    @topological_dimension.setter
    def topological_dimension(self, topological_dimension: float):
        """Sets the topological_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.

        Sum of dimensions of topological primitives of zones defined by this DGGS.  # noqa: E501

        :param topological_dimension: The topological_dimension of this DggsRsParametersDggsRsStructureZoneGeometry.
        :type topological_dimension: float
        """

        self._topological_dimension = topological_dimension
