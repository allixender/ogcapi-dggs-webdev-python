# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server import util


class MultipointGeoJSON(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, coordinates: List[List[float]]=None):  # noqa: E501
        """MultipointGeoJSON - a model defined in Swagger

        :param type: The type of this MultipointGeoJSON.  # noqa: E501
        :type type: str
        :param coordinates: The coordinates of this MultipointGeoJSON.  # noqa: E501
        :type coordinates: List[List[float]]
        """
        self.swagger_types = {
            'type': str,
            'coordinates': List[List[float]]
        }

        self.attribute_map = {
            'type': 'type',
            'coordinates': 'coordinates'
        }
        self._type = type
        self._coordinates = coordinates

    @classmethod
    def from_dict(cls, dikt) -> 'MultipointGeoJSON':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The multipointGeoJSON of this MultipointGeoJSON.  # noqa: E501
        :rtype: MultipointGeoJSON
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this MultipointGeoJSON.


        :return: The type of this MultipointGeoJSON.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this MultipointGeoJSON.


        :param type: The type of this MultipointGeoJSON.
        :type type: str
        """
        allowed_values = ["MultiPoint"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def coordinates(self) -> List[List[float]]:
        """Gets the coordinates of this MultipointGeoJSON.


        :return: The coordinates of this MultipointGeoJSON.
        :rtype: List[List[float]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: List[List[float]]):
        """Sets the coordinates of this MultipointGeoJSON.


        :param coordinates: The coordinates of this MultipointGeoJSON.
        :type coordinates: List[List[float]]
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates
