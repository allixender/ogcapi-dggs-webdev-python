# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server.models.dggsjson import DGGSJSON  # noqa: F401,E501
from dggs_api_server.models.link import Link  # noqa: F401,E501
from dggs_api_server.models.number_matched import NumberMatched  # noqa: F401,E501
from dggs_api_server.models.number_returned import NumberReturned  # noqa: F401,E501
from dggs_api_server.models.time_stamp import TimeStamp  # noqa: F401,E501
from dggs_api_server import util


class ZoneCollectionDGGSJSON(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, features: List[DGGSJSON]=None, links: List[Link]=None, time_stamp: TimeStamp=None, number_matched: NumberMatched=None, number_returned: NumberReturned=None):  # noqa: E501
        """ZoneCollectionDGGSJSON - a model defined in Swagger

        :param type: The type of this ZoneCollectionDGGSJSON.  # noqa: E501
        :type type: str
        :param features: The features of this ZoneCollectionDGGSJSON.  # noqa: E501
        :type features: List[DGGSJSON]
        :param links: The links of this ZoneCollectionDGGSJSON.  # noqa: E501
        :type links: List[Link]
        :param time_stamp: The time_stamp of this ZoneCollectionDGGSJSON.  # noqa: E501
        :type time_stamp: TimeStamp
        :param number_matched: The number_matched of this ZoneCollectionDGGSJSON.  # noqa: E501
        :type number_matched: NumberMatched
        :param number_returned: The number_returned of this ZoneCollectionDGGSJSON.  # noqa: E501
        :type number_returned: NumberReturned
        """
        self.swagger_types = {
            'type': str,
            'features': List[DGGSJSON],
            'links': List[Link],
            'time_stamp': TimeStamp,
            'number_matched': NumberMatched,
            'number_returned': NumberReturned
        }

        self.attribute_map = {
            'type': 'type',
            'features': 'features',
            'links': 'links',
            'time_stamp': 'timeStamp',
            'number_matched': 'numberMatched',
            'number_returned': 'numberReturned'
        }
        self._type = type
        self._features = features
        self._links = links
        self._time_stamp = time_stamp
        self._number_matched = number_matched
        self._number_returned = number_returned

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneCollectionDGGSJSON':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The zoneCollectionDGGSJSON of this ZoneCollectionDGGSJSON.  # noqa: E501
        :rtype: ZoneCollectionDGGSJSON
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ZoneCollectionDGGSJSON.


        :return: The type of this ZoneCollectionDGGSJSON.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ZoneCollectionDGGSJSON.


        :param type: The type of this ZoneCollectionDGGSJSON.
        :type type: str
        """
        allowed_values = ["FeatureCollection"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def features(self) -> List[DGGSJSON]:
        """Gets the features of this ZoneCollectionDGGSJSON.


        :return: The features of this ZoneCollectionDGGSJSON.
        :rtype: List[DGGSJSON]
        """
        return self._features

    @features.setter
    def features(self, features: List[DGGSJSON]):
        """Sets the features of this ZoneCollectionDGGSJSON.


        :param features: The features of this ZoneCollectionDGGSJSON.
        :type features: List[DGGSJSON]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def links(self) -> List[Link]:
        """Gets the links of this ZoneCollectionDGGSJSON.


        :return: The links of this ZoneCollectionDGGSJSON.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links: List[Link]):
        """Sets the links of this ZoneCollectionDGGSJSON.


        :param links: The links of this ZoneCollectionDGGSJSON.
        :type links: List[Link]
        """

        self._links = links

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this ZoneCollectionDGGSJSON.


        :return: The time_stamp of this ZoneCollectionDGGSJSON.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this ZoneCollectionDGGSJSON.


        :param time_stamp: The time_stamp of this ZoneCollectionDGGSJSON.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp

    @property
    def number_matched(self) -> NumberMatched:
        """Gets the number_matched of this ZoneCollectionDGGSJSON.


        :return: The number_matched of this ZoneCollectionDGGSJSON.
        :rtype: NumberMatched
        """
        return self._number_matched

    @number_matched.setter
    def number_matched(self, number_matched: NumberMatched):
        """Sets the number_matched of this ZoneCollectionDGGSJSON.


        :param number_matched: The number_matched of this ZoneCollectionDGGSJSON.
        :type number_matched: NumberMatched
        """

        self._number_matched = number_matched

    @property
    def number_returned(self) -> NumberReturned:
        """Gets the number_returned of this ZoneCollectionDGGSJSON.


        :return: The number_returned of this ZoneCollectionDGGSJSON.
        :rtype: NumberReturned
        """
        return self._number_returned

    @number_returned.setter
    def number_returned(self, number_returned: NumberReturned):
        """Sets the number_returned of this ZoneCollectionDGGSJSON.


        :param number_returned: The number_returned of this ZoneCollectionDGGSJSON.
        :type number_returned: NumberReturned
        """

        self._number_returned = number_returned
