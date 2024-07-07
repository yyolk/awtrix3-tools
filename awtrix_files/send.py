"""
from awtrix_files.send import post_multipart
from awtrix_files.la_icon import get_lametric_icon

filename, bo = bet_lametric_icon(66)
resp = post_multipart("https://webhook.site/6c6d7caf-aba6-43b2-9cb8-41158108c727", bo, filename)
"""
import urllib.request
import mimetypes
import uuid

from io import BytesIO


def post_multipart(url, bo: BytesIO, file_name: str):
    # URL="http://$IP_ADDRESS/edit"
    # curl -X POST -F "file=@$TEMP_FILE;filename=/ICONS/$FILE_NAME" "$URL"
    #                         ^-- bytes          ^
    #                                            |
    #                                            \- destination filepath

    # The file to be uploaded
    file_path = f"/ICONS/{file_name}"

    # Generate a boundary string
    boundary = uuid.uuid4().hex
    # boundary_bytes = boundary.encode('utf-8')

    bo.seek(0)
    file_content = bo.getvalue()

    # Determine the file's MIME type
    mime_type = mimetypes.guess_type(file_name)[0]  # or 'application/octet-stream'

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
