# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server import util


class ConfClasses(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, conforms_to: List[str]=None):  # noqa: E501
        """ConfClasses - a model defined in Swagger

        :param conforms_to: The conforms_to of this ConfClasses.  # noqa: E501
        :type conforms_to: List[str]
        """
        self.swagger_types = {
            'conforms_to': List[str]
        }

        self.attribute_map = {
            'conforms_to': 'conformsTo'
        }
        self._conforms_to = conforms_to

    @classmethod
    def from_dict(cls, dikt) -> 'ConfClasses':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The confClasses of this ConfClasses.  # noqa: E501
        :rtype: ConfClasses
        """
        return util.deserialize_model(dikt, cls)

    @property
    def conforms_to(self) -> List[str]:
        """Gets the conforms_to of this ConfClasses.


        :return: The conforms_to of this ConfClasses.
        :rtype: List[str]
        """
        return self._conforms_to

    @conforms_to.setter
    def conforms_to(self, conforms_to: List[str]):
        """Sets the conforms_to of this ConfClasses.


        :param conforms_to: The conforms_to of this ConfClasses.
        :type conforms_to: List[str]
        """
        if conforms_to is None:
            raise ValueError("Invalid value for `conforms_to`, must not be `None`")  # noqa: E501

        self._conforms_to = conforms_to
