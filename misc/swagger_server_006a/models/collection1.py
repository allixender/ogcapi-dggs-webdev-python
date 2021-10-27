# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dggs_api_server.models.base_model_ import Model
from dggs_api_server.models.extent import Extent  # noqa: F401,E501
from dggs_api_server.models.keyword import Keyword  # noqa: F401,E501
from dggs_api_server import util


class Collection1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: str=None, description: str=None, keywords: List[Keyword]=None, attribution: str=None, extent: Extent=None, crs: List[str]=None):  # noqa: E501
        """Collection1 - a model defined in Swagger

        :param id: The id of this Collection1.  # noqa: E501
        :type id: str
        :param title: The title of this Collection1.  # noqa: E501
        :type title: str
        :param description: The description of this Collection1.  # noqa: E501
        :type description: str
        :param keywords: The keywords of this Collection1.  # noqa: E501
        :type keywords: List[Keyword]
        :param attribution: The attribution of this Collection1.  # noqa: E501
        :type attribution: str
        :param extent: The extent of this Collection1.  # noqa: E501
        :type extent: Extent
        :param crs: The crs of this Collection1.  # noqa: E501
        :type crs: List[str]
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'description': str,
            'keywords': List[Keyword],
            'attribution': str,
            'extent': Extent,
            'crs': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'keywords': 'keywords',
            'attribution': 'attribution',
            'extent': 'extent',
            'crs': 'crs'
        }
        self._id = id
        self._title = title
        self._description = description
        self._keywords = keywords
        self._attribution = attribution
        self._extent = extent
        self._crs = crs

    @classmethod
    def from_dict(cls, dikt) -> 'Collection1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The collection_1 of this Collection1.  # noqa: E501
        :rtype: Collection1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Collection1.

        identifier of the collection used, for example, in URIs  # noqa: E501

        :return: The id of this Collection1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Collection1.

        identifier of the collection used, for example, in URIs  # noqa: E501

        :param id: The id of this Collection1.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Collection1.

        human readable title of the collection  # noqa: E501

        :return: The title of this Collection1.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Collection1.

        human readable title of the collection  # noqa: E501

        :param title: The title of this Collection1.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Collection1.

        a description of the collection  # noqa: E501

        :return: The description of this Collection1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Collection1.

        a description of the collection  # noqa: E501

        :param description: The description of this Collection1.
        :type description: str
        """

        self._description = description

    @property
    def keywords(self) -> List[Keyword]:
        """Gets the keywords of this Collection1.

        keywords about the elements in the collection  # noqa: E501

        :return: The keywords of this Collection1.
        :rtype: List[Keyword]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords: List[Keyword]):
        """Sets the keywords of this Collection1.

        keywords about the elements in the collection  # noqa: E501

        :param keywords: The keywords of this Collection1.
        :type keywords: List[Keyword]
        """

        self._keywords = keywords

    @property
    def attribution(self) -> str:
        """Gets the attribution of this Collection1.

        The provider of the source data for the collection. Map viewers normally show this information at the bottom of the map  # noqa: E501

        :return: The attribution of this Collection1.
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution: str):
        """Sets the attribution of this Collection1.

        The provider of the source data for the collection. Map viewers normally show this information at the bottom of the map  # noqa: E501

        :param attribution: The attribution of this Collection1.
        :type attribution: str
        """

        self._attribution = attribution

    @property
    def extent(self) -> Extent:
        """Gets the extent of this Collection1.


        :return: The extent of this Collection1.
        :rtype: Extent
        """
        return self._extent

    @extent.setter
    def extent(self, extent: Extent):
        """Sets the extent of this Collection1.


        :param extent: The extent of this Collection1.
        :type extent: Extent
        """

        self._extent = extent

    @property
    def crs(self) -> List[str]:
        """Gets the crs of this Collection1.

        The list of coordinate reference systems supported by the service. The first item is the default coordinate reference system.  # noqa: E501

        :return: The crs of this Collection1.
        :rtype: List[str]
        """
        return self._crs

    @crs.setter
    def crs(self, crs: List[str]):
        """Sets the crs of this Collection1.

        The list of coordinate reference systems supported by the service. The first item is the default coordinate reference system.  # noqa: E501

        :param crs: The crs of this Collection1.
        :type crs: List[str]
        """

        self._crs = crs