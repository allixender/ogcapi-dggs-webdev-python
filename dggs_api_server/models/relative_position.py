# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server import util


class RelativePosition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BEFORE = "Before"
    AFTER = "After"
    MEETS = "Meets"
    METBY = "MetBy"
    OVERLAPS = "Overlaps"
    OVERLAPPEDBY = "OverlappedBy"
    STARTS = "Starts"
    STARTEDBY = "StartedBy"
    DURING = "During"
    CONTAINS = "Contains"
    FINISHES = "Finishes"
    FINISHEDBY = "FinishedBy"
    EQUALS = "Equals"
    IN = "In"
    DISJOINT = "Disjoint"
    def __init__(self):  # noqa: E501
        """RelativePosition - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'RelativePosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RelativePosition of this RelativePosition.  # noqa: E501
        :rtype: RelativePosition
        """
        return util.deserialize_model(dikt, cls)
