class InjectionRequest(object):
    """
    Represents a injection request for sending to the Injection Api.
    To be serialized into JSON string before sending to the Injection Api.
    """

    def __init__(self, server_id: int, api_key: str, messages: list):
        """
        Initializes a new instance of the AddressJson class
        :param server_id: Your SocketLabs ServerId number.
        :type server_id: str
        :param api_key: Your SocketLabs Injection API key.
        :type api_key: str
        :param messages: the list of messages (MessageJson) to send. This library is limited to one
        :type messages: list
        """
        self._api_key = api_key
        self._server_id = server_id
        self._messages = messages

    @property
    def server_id(self):
        """
        Sets the server id for the injection Request.
        :return the server id
        :rtype int
        """
        return self._server_id

    @property
    def api_key(self):
        """
        Gets the SocketLabs Injection API key for the Injection Request.
        :return the api key
        :rtype str
        """
        return self._api_key

    @property
    def messages(self):
        """
        Gets the list of messages to be sent.
        :return the list of messages
        :rtype list
        """
        return self._messages

    def to_json(self):
        """
        build json dict for the InjectionRequest.
        :return the json dictionary
        :rtype dict
        """
        json = {
            "serverId":  str(self._server_id),
            "apiKey": self._api_key,
        }
        if len(self._messages) > 0:
            e = []
            for m in self._messages:
                e.append(m.to_json())
            json["messages"] = e
        return json
