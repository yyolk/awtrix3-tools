import mimetypes
import urllib.parse
import urllib.request

from io import BytesIO
from typing import Iterator, Union


def download_file_in_chunks(
    url: str, chunk_size: int = 1024
) -> Iterator[Union[dict[str], bytes]]:
    """Download a file with HTTP GET given a URL in chunks.

    Args:
        url: The URL to the resource to download.
        chunk_size: The amount of bytes per chunk to return. Defaults to 1024.

    Yields:
        Always yields the headers first, then all subsequent yields are the chunks of the resource.
    """
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
    """Save a BytesIO to a filename.

    Args:
        bo: BytesIO (fp-like) to write.
        filename: The filename to write to, can also be a path.
    """
    # Rewind the tape
    bo.seek(0)
    # Write the file to filename
    with open(filename, "wb") as fp:
        fp.write(bo.read())


def get_filename_and_bytesio(url) -> tuple[str, BytesIO]:
    """Fetch and return the filename and the resource's tape.

    Args:
        url: The URL to fetch.

    Returns:
        str: The filename of the resource that was fetched (extracted from the URL).
        BytesIO: The contents of the file in a seekable format.
    """
    bo = BytesIO()
    headers, *chunker = download_file_in_chunks(url)
    filetype = mimetypes.guess_extension(headers["content-type"])
    # TODO: fallback to unique name based off url hash or file chunk hash or header hash
    name = urllib.parse.urlsplit(url).path.split("/")[-1]
    filename = f"{name}{filetype}"
    for chunk in chunker:
        bo.write(chunk)
    return filename, bo
