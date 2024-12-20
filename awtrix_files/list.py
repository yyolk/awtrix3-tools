import json
import urllib.request

from dataclasses import dataclass

import ada_url

from uritemplate import URITemplate


awtrix_uri_template = URITemplate("http://{awtrix_host}{/path=list}{/filename}{?dir}")


@dataclass(frozen=True)
class Icon:
    name: str
    path: str


@dataclass(frozen=True)
class HostIcon:
    host: str
    icon: Icon


def _list(host, dir_) -> list[dict[str, str]]:
    """Main function for listing.

    All files in AWTRIX are served through JSON responses at certain paths.

    Args:
        host: The AWTRIX 3 host
        dir_: The directory to list

    Returns:
        A list of key value pairs that are files at the specified directory (path).
    """
    with urllib.request.urlopen(
        awtrix_uri_template.expand(awtrix_host=host, dir=dir_)
    ) as resp:
        return json.load(resp)


def list_icons(host, dir_="/ICONS") -> set[Icon]:
    result_set = set()
    for icon in _list(host, dir_):
        url = ada_url.URL(
            awtrix_uri_template.expand(
                awtrix_host=host, path="ICONS", filename=icon["name"]
            )
        )
        icon = Icon(
            name=icon["name"],
            path=url.pathname,
        )
        result_set.add(icon)
    return result_set


def list_melodies(host, dir_="/MELODIES") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_palettes(host, dir_="/PALETTES") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_customapps(host, dir_="/CUSTOMAPPS") -> list[dict[str, str]]:
    return _list(host, dir_)
