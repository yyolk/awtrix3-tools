import argparse
import urllib.request
import json

from uritemplate import URITemplate

parser = argparse.parser()

parser.add_argument("host", help="the hostname for the awtrix device")

args = parser.parse_args()

awtrix_uri = URITemplate("http://{awtrix_host}{/path}{?dir}")

with urllib.request.urlopen(awtrix_uri.expand(awtrix_host=args.host, dir="/ICONS")) as resp:
    body = json.load(resp)

print(body)