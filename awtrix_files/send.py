import mimetypes
import urllib.request
import uuid

from io import BytesIO


def post_multipart(url, bo: BytesIO, filename: str) -> bytes:
    """Utility for uploading files using AWTRIX 3's embededd web server.

    The AWTRIX 3's embedded webserver will accept POST requests.
    In the future it could also accept PUT requests, which would be the appropriate method to use.

    Notes:
        Here's the breakdown of this function using curl as a reference.
        URL="http://$IP_ADDRESS/edit"
        curl -X POST -F "file=@$TEMP_FILE;filename=/ICONS/$filename" "$URL"
                                ^-- bytes          ^
                                                   |- destination filepath
    Args:
        url: The destination URL to POST the multipart form to.
        bo: The BytesIO object (seekable file) to send.
        filename: The destination filename to save upload as.

    Returns:
        The response bytes from the HTTP POST request.
    """
    # The file to be uploaded
    file_path = f"/ICONS/{filename}"

    # Generate a boundary string
    boundary = uuid.uuid4().hex
    # boundary_bytes = boundary.encode('utf-8')

    bo.seek(0)
    file_content = bo.getvalue()

    # Determine the file's MIME type
    mime_type = mimetypes.guess_type(filename)[0]  # or 'application/octet-stream'

    # Create the multipart/form-data body
    data = [
        f"--{boundary}",
        f'Content-Disposition: form-data; name="file"; filename="{file_path}"',
        f"Content-Type: {mime_type}",
        "",
        file_content,
        f"--{boundary}--",
        "",
    ]
    body = b"\r\n".join(
        part.encode("utf-8") if isinstance(part, str) else part for part in data
    )

    # Create the request object
    request = urllib.request.Request(url, data=body)
    request.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    request.add_header("Content-Length", str(len(body)))

    # Send the request and get the response
    with urllib.request.urlopen(request) as response:
        response_data = response.read()

    return response_data
