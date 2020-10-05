import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def server_javaicon_get(server, port=None):  # noqa: E501
    """server_javaicon_get

    generated motd for the server # noqa: E501

    :param server: ip or hostname of the server
    :type server: str
    :param port: port of the server
    :type port: int

    :rtype: str
    """
    return 'do some magic!'


def servers_bedrock_get(server, port=None):  # noqa: E501
    """servers_bedrock_get

    returns info about a minecraft server # noqa: E501

    :param server: ip or hostname of the server
    :type server: str
    :param port: port of the server
    :type port: int

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def servers_java_get(server, port=None):  # noqa: E501
    """servers_java_get

    returns info about a minecraft server # noqa: E501

    :param server: ip or hostname of the server
    :type server: str
    :param port: port of the server
    :type port: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'
