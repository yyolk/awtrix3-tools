import urllib.request
import json

from uritemplate import URITemplate


awtrix_uri_template = URITemplate("http://{awtrix_host}{/path=list}{?dir}")


def list_icons(host, dir_="/ICONS") -> list[dict[str, str]]:
    with urllib.request.urlopen(
        awtrix_uri_template.expand(awtrix_host=host, dir=dir_)
    ) as resp:
        return json.load(resp)