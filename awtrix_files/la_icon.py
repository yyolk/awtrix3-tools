import mimetypes
import urllib.request

from io import BytesIO
from typing import Iterator, Union

from uritemplate import URITemplate


lametric_icon_uri_template = URITemplate("https://developer.lametric.com/content/apps/icon_thumbs{/icon}")


def download_file_in_chunks(url: str, chunk_size: int = 1024) -> Iterator[Union[dict, bytes, ...]]:
    with urllib.request.urlopen(url) as response:
        yield response.headers
        while True:
            # Read a chunk of data
            chunk = response.read(chunk_size)
            if not chunk:
                break
            yield chunk

def get_lametric_icon(icon: int) -> (str, BytesIO):
    bo = BytesIO()
    headers, *chunker = download_file_in_chunks(lametric_icon_uri_template.expand(icon=icon))
    filetype = mimetypes.guess_extension(headers["content-type"])
    filename = f"{icon}{filetype}"
    for chunk in chunker:
        bo.write(chunk)
    return filename, bo

def save_bytesio_to_file(bo: BytesIO, filename: str):
    # Rewind the tape
    bo.seek(0)
    with open(filename, "wb") as fp:
        fp.write(bo.read())


if __name__ == "__main__":
    filename, bo = get_lametric_icon(66)
    print(f"{filename=}")