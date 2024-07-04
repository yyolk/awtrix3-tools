import base64

from io import BytesIO

from PIL import Image
from uritemplate import URITemplate

from awtrix_files.fetch import get_filename_and_bytesio


lametric_icon_uri_template = URITemplate(
    "https://developer.lametric.com/content/apps/icon_thumbs{/icon}"
)


def get_lametric_icon(icon: int) -> (str, "BytesIO"):
    url = lametric_icon_uri_template.expand(icon=icon)
    return get_filename_and_bytesio(url)


def bytesio_image_to_base64(bo: BytesIO, gif_seek=1) -> str:
    bo.seek(0)
    pil_im = Image.open(bo)
    if pil_im.format == "GIF":
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
