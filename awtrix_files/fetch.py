from io import BytesIO
import urllib.request
from typing import Iterator, Union


def download_file_in_chunks(url: str, chunk_size: int = 1024) -> Iterator[Union[dict, bytes, ...]]:
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