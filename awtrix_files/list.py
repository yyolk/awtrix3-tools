import urllib.request
import json

from uritemplate import URITemplate


awtrix_uri_template = URITemplate("http://{awtrix_host}{/path=list}{?dir}")


def _list(host, dir_) -> list[dict[str, str]]:
    with urllib.request.urlopen(
        awtrix_uri_template.expand(awtrix_host=host, dir=dir_)
    ) as resp:
        return json.load(resp)


def list_icons(host, dir_="/ICONS") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_melodies(host, dir_="/MELODIES") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_palettes(host, dir_="/PALETTES") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_customapps(host, dir_="/CUSTOMAPPS") -> list[dict[str, str]]:
    return _list(host, dir_)