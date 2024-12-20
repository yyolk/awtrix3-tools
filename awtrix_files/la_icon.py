import base64

from io import BytesIO

from PIL import Image
from uritemplate import URITemplate

from awtrix_files.fetch import get_filename_and_bytesio


lametric_icon_uri_template = URITemplate(
    "https://developer.lametric.com/content/apps/icon_thumbs{/icon}"
)


def get_lametric_icon(icon: int) -> tuple[str, BytesIO]:
    """Get an icon from LAMetric's icon index.

    Args:
        icon: The icon number to fetch.

    Returns:
        str: The icon's filename (the number with extension).
        BytesIO: The seekable icon content.
    """
    url = lametric_icon_uri_template.expand(icon=icon)
    return get_filename_and_bytesio(url)


def bytesio_image_to_base64(bo: BytesIO, gif_seek=1) -> str:
    """Utility function for sending as Base64 encoded.

    Via the docs https://blueforcer.github.io/awtrix3/#/api:
        The icon ID or filename (without extension) to display on the app.
        You can also send a 8x8 jpg as Base64 String

    Args:
        bo: The BytesIO (filestream) to send.
        gif_seek: The frame to use from a gif image. Defaults to 1.

    Returns:
        The Base64 encoded image to be used to send for sending attached to a message payload.
    """
    # rewind the tape
    bo.seek(0)
    pil_im = Image.open(bo)
    if pil_im.format == "GIF":
        # Take the single frame to represent the gif
        pil_im.seek(pil_im.tell() + gif_seek)
    pil_im = pil_im.convert("RGB")
    newb = BytesIO()
    pil_im.save(newb, "jpeg")
    im_bytes = newb.getvalue()
    return base64.b64encode(im_bytes).decode()


if __name__ == "__main__":
    filename, bo = get_lametric_icon(66)
    print(f"{filename=}")
    print(bytesio_image_to_base64(bo))
