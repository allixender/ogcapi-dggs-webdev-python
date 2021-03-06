# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server.models.link import Link  # noqa: F401,E501
from dggs_api_server.models.number_matched import NumberMatched  # noqa: F401,E501
from dggs_api_server.models.number_returned import NumberReturned  # noqa: F401,E501
from dggs_api_server.models.time_stamp import TimeStamp  # noqa: F401,E501
from dggs_api_server import util


class ZoneList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, zones: List[str]=None, links: List[Link]=None, time_stamp: TimeStamp=None, number_matched: NumberMatched=None, number_returned: NumberReturned=None):  # noqa: E501
        """ZoneList - a model defined in Swagger

        :param zones: The zones of this ZoneList.  # noqa: E501
        :type zones: List[str]
        :param links: The links of this ZoneList.  # noqa: E501
        :type links: List[Link]
        :param time_stamp: The time_stamp of this ZoneList.  # noqa: E501
        :type time_stamp: TimeStamp
        :param number_matched: The number_matched of this ZoneList.  # noqa: E501
        :type number_matched: NumberMatched
        :param number_returned: The number_returned of this ZoneList.  # noqa: E501
        :type number_returned: NumberReturned
        """
        self.swagger_types = {
            'zones': List[str],
            'links': List[Link],
            'time_stamp': TimeStamp,
            'number_matched': NumberMatched,
            'number_returned': NumberReturned
        }

        self.attribute_map = {
            'zones': 'zones',
            'links': 'links',
            'time_stamp': 'timeStamp',
            'number_matched': 'numberMatched',
            'number_returned': 'numberReturned'
        }
        self._zones = zones
        self._links = links
        self._time_stamp = time_stamp
        self._number_matched = number_matched
        self._number_returned = number_returned

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The zoneList of this ZoneList.  # noqa: E501
        :rtype: ZoneList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zones(self) -> List[str]:
        """Gets the zones of this ZoneList.


        :return: The zones of this ZoneList.
        :rtype: List[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones: List[str]):
        """Sets the zones of this ZoneList.


        :param zones: The zones of this ZoneList.
        :type zones: List[str]
        """
        if zones is None:
            raise ValueError("Invalid value for `zones`, must not be `None`")  # noqa: E501

        self._zones = zones

    @property
    def links(self) -> List[Link]:
        """Gets the links of this ZoneList.


        :return: The links of this ZoneList.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links: List[Link]):
        """Sets the links of this ZoneList.


        :param links: The links of this ZoneList.
        :type links: List[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this ZoneList.


        :return: The time_stamp of this ZoneList.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this ZoneList.


        :param time_stamp: The time_stamp of this ZoneList.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp

    @property
    def number_matched(self) -> NumberMatched:
        """Gets the number_matched of this ZoneList.


        :return: The number_matched of this ZoneList.
        :rtype: NumberMatched
        """
        return self._number_matched

    @number_matched.setter
    def number_matched(self, number_matched: NumberMatched):
        """Sets the number_matched of this ZoneList.


        :param number_matched: The number_matched of this ZoneList.
        :type number_matched: NumberMatched
        """

        self._number_matched = number_matched

    @property
    def number_returned(self) -> NumberReturned:
        """Gets the number_returned of this ZoneList.


        :return: The number_returned of this ZoneList.
        :rtype: NumberReturned
        """
        return self._number_returned

    @number_returned.setter
    def number_returned(self, number_returned: NumberReturned):
        """Sets the number_returned of this ZoneList.


        :param number_returned: The number_returned of this ZoneList.
        :type number_returned: NumberReturned
        """

        self._number_returned = number_returned
