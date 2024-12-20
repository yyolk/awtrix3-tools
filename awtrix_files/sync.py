"""Holds syncing the files of one awtrix3 to another awtrix3.

TODO:
    - use this for holding the logic for syncing
"""

from awtrix_files.list import Icon, list_icons


def difference_icon_list(host1: str, host2: str) -> set[Icon]:
    """Get the difference of the two set[Icon] of two hosts.

    This will only return the larger set[Icon]. Where if one set[Icon]
    is in the larger set[Icon], the difference comes down to which ones
    aren't yet synced to the smaller set.
    TODO:
        - A better implementation that does a more comprehensive compare.
    """
    host1_icons = list_icons(host1)
    host2_icons = list_icons(host2)
    return max([host1_icons - host2_icons, host2_icons - host1_icons])
