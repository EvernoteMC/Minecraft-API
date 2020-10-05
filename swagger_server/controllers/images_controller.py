import connexion
import six

from swagger_server import util


def images_advancement_get(text, item=None, title=None):  # noqa: E501
    """create a minecraft acheivement

     # noqa: E501

    :param text: acheivement text
    :type text: str
    :param item: choose what item is shown
    :type item: str
    :param title: title of acheivement
    :type title: str

    :rtype: str
    """
    return "do some magic!"


def images_book_get(text):  # noqa: E501
    """create a page from a minecraft book

     # noqa: E501

    :param text: text to fill the book
    :type text: str

    :rtype: str
    """
    return "do some magic!"


def images_death_get(message, xp):  # noqa: E501
    """Create a custom death screen

     # noqa: E501

    :param message: death message
    :type message: str
    :param xp: score to show
    :type xp: int

    :rtype: str
    """
    return "do some magic!"


def images_motd_get(text):  # noqa: E501
    """View motd

     # noqa: E501

    :param text: motd text
    :type text: str

    :rtype: str
    """
    return "do some magic!"


def images_sign_get(line1, wood=None, line2=None, line3=None, line4=None):  # noqa: E501
    """create an sign.png

     # noqa: E501

    :param line1: first line of the sign
    :type line1: str
    :param wood: choose what type of wood the sign should be
    :type wood: str
    :param line2: second line of the sign
    :type line2: str
    :param line3: third line of the sign
    :type line3: str
    :param line4: fourth line of the sign
    :type line4: str

    :rtype: str
    """
    return "do some magic!"


def images_splashscreen_get(text):  # noqa: E501
    """Create a custom minecraft splashscreen

     # noqa: E501

    :param text: text on splashscreen
    :type text: str

    :rtype: str
    """
    return "do some magic!"
