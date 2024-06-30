import mimetypes
import urllib.request

from uritemplate import URITemplate


lametric_icon_uri_template = URITemplate("https://developer.lametric.com/content/apps/icon_thumbs{/icon}")

filename, headers = urllib.request.urlretrieve(lametric_icon_uri_template.expand(icon=66))

filetype = mimetypes.guess_extension(headers["Content-Type"])

print(f"{filetype} image saved to {filename}.")