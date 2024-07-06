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
