# awtrix3-tools
Tools for managing an AWTRIX 3 Smart Clock

# Notes

```
from awtrix_files.fetch import get_filename_and_bytesio, save_bytesio_to_file
office_url = awtrix_uri_template.expand(awtrix_host=office_host, path="")
In [58]: office_url
Out[58]: 'http://awtrix_host.local/'
In [61]: def save_icons_locally(icons):
    ...:     for i in icons:
    ...:         url = f"{office_url}/{i.path}?download=true"
    ...:         _, bo = get_filename_and_bytesio(url)
    ...:         save_bytesio_to_file(bo, i.name)
    ...: 
In [68]: living_room_url = "http://living-room.local"

from awtrix_files.send import post_multipart                                     
In [69]: def save_icons_directly(icons):
    ...:     for i in icons:
    ...:         url = f"{office_url}/{i.path}?download=true"
    ...:         _, bo = get_filename_and_bytesio(url)
    ...:         resp = post_multipart(f"{living_room_url}/edit", bo, i.name)
    ...:         print(resp)
    ...: 
In [70]: save_icons_directly(missing_icons)
```
                                       