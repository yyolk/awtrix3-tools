import mimetypes
import urllib.request
import urllib.parse

from io import BytesIO
from typing import Iterator, Union


def download_file_in_chunks(
    url: str, chunk_size: int = 1024
) -> "Iterator[Union[dict, bytes, ...]]":  # type: ignore
    with urllib.request.urlopen(url) as response:
        # Yield the headers first
        yield response.headers
        while True:
            # Read a chunk of data
            chunk = response.read(chunk_size)
            if not chunk:
                break
            # Yield a chunk of data
            yield chunk


def save_bytesio_to_file(bo: BytesIO, filename: str):
    # Rewind the tape
    bo.seek(0)
    # Write the file to filename
    with open(filename, "wb") as fp:
        fp.write(bo.read())


def get_filename_and_bytesio(url) -> tuple[str, BytesIO]:
    bo = BytesIO()
    headers, *chunker = download_file_in_chunks(url)
    filetype = mimetypes.guess_extension(headers["content-type"])
    # TODO: fallback to unique name based off url hash or file chunk hash or header hash
    name = urllib.parse.urlsplit(url).path.split("/")[-1]
    filename = f"{name}{filetype}"
    for chunk in chunker:
        bo.write(chunk)
    return filename, bo
