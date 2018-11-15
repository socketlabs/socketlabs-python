from .mergefieldjson import MergeFieldJson


class MergeDataJson(object):
    """
    Represents MergeData for a single message.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self, per_message: list = None, global_merge_data: list = None):
        """
        Creates a new instance of the MergeDataJson class.
        :param per_message: the per message merge data list
        :type per_message: list
        :param global_merge_data: the list of global merge data
        :type global_merge_data: list
        """
        self._per_message = per_message
        self._global = global_merge_data

    @property
    def per_message_merge_data(self):
        """
        Get merge field data for each message.
        :return the per message merge data list
        :rtype list
        """
        return self._per_message

    @per_message_merge_data.setter
    def per_message_merge_data(self, val: list):
        """
        Set merge field data for each message.
        :param val: the per message merge data list
        :type val: list
        """
        self._per_message = []
        if val is not None:
            for item in val:
                if isinstance(item, list):
                    l1 = []
                    for i2 in val:
                        if isinstance(item, MergeFieldJson):
                            l1.append(i2)
                    self._per_message.append(l1)

    @property
    def global_merge_data(self):
        """
        Get merge field data for all messages in the request
        :return the list of global merge data
        :rtype list
        """
        return self._global

    @global_merge_data.setter
    def global_merge_data(self, val: list):
        """
        Set merge field data for all messages in the request
        :param val: the list of global merge data
        :type val: list
        """
        self._global = []
        if val is not None:
            for item in val:
                if isinstance(item, MergeFieldJson):
                    self._global.append(item)

    def to_json(self):
        """
        build json dict for MergeDataJson
        :return the json dictionary
        :rtype dict
        """
        json = {}

        if len(self._global) > 0:
            e = []
            for i in self._global:
                e.append(i.to_json())
            json["global"] = e

        if len(self._per_message) > 0:
            e = []
            for message in self._per_message:
                m = []
                for i in message:
                    m.append(i.to_json())
                e.append(m)
            json["perMessage"] = e

        return json
