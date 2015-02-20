__author__ = 'Odd'

from os import path
import re


def clean_filename(filename, unicode=True):
    """
    Removes invalid characters that should work on pretty much all platforms.
    Optionally possible to remove unicode characters

    >>> clean_filename('hø el\\nl-o.mkv')
    'hø ell-o.mkv'
    >>> clean_filename("hø el\\nl-o.txt", False)
    'h ell-o.txt'

    :param filename: Filename; can contain extension
    :param unicode: Enable or disable unicode characters?
    :return: Valid filename
    """
    keep_characters = [' ', '_', '-']
    filename_split = path.splitext(filename)
    if unicode:
        new_name = "".join(c for c in filename_split[0] if c.isalnum() or c in keep_characters) + filename_split[1]
    else:
        new_name = "".join(c for c in filename_split[0] if re.fullmatch("[0-z]", c) is not None or
                           c in keep_characters) + filename_split[1]
    return new_name[0:255]

if __name__ == "__main__":
    import doctest
    doctest.testmod()