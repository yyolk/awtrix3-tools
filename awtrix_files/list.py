import urllib.request
import json

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
    with urllib.request.urlopen(
        awtrix_uri_template.expand(awtrix_host=host, dir=dir_)
    ) as resp:
        return json.load(resp)


def list_icons(host, dir_="/ICONS") -> set[Icon]:
    return {
        Icon(
            name=icon["name"],
            path=ada_url.URL(
                awtrix_uri_template.expand(
                    awtrix_host=host, path="ICONS", filename=icon["name"]
                )
            ).pathname,
        )
        for icon in _list(host, dir_)
    }


def list_melodies(host, dir_="/MELODIES") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_palettes(host, dir_="/PALETTES") -> list[dict[str, str]]:
    return _list(host, dir_)


def list_customapps(host, dir_="/CUSTOMAPPS") -> list[dict[str, str]]:
    return _list(host, dir_)
