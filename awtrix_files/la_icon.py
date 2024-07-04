from uritemplate import URITemplate

from awtrix_files.fetch import get_filename_and_bytesio


lametric_icon_uri_template = URITemplate(
    "https://developer.lametric.com/content/apps/icon_thumbs{/icon}"
)


def get_lametric_icon(icon: int) -> (str, "BytesIO"):
    url = lametric_icon_uri_template.expand(icon=icon)
    return get_filename_and_bytesio(url)


if __name__ == "__main__":
    filename, _ = get_lametric_icon(66)
    print(f"{filename=}")
