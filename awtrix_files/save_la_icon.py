import mimetypes
import os
import urllib.request

from uritemplate import URITemplate


lametric_icon_uri_template = URITemplate("https://developer.lametric.com/content/apps/icon_thumbs{/icon}")

filename, headers = urllib.request.urlretrieve(lametric_icon_uri_template.expand(icon=66))

filetype = mimetypes.guess_extension(headers["Content-Type"])
new_filename = f"{filename}{filetype}"
os.rename(filename, new_filename)

print(f"image saved to {new_filename}")