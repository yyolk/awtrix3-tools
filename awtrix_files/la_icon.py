import mimetypes

from io import BytesIO

from uritemplate import URITemplate

from awtrix_files.fetch import download_file_in_chunks


lametric_icon_uri_template = URITemplate("https://developer.lametric.com/content/apps/icon_thumbs{/icon}")


def get_lametric_icon(icon: int) -> (str, BytesIO):
    bo = BytesIO()
    headers, *chunker = download_file_in_chunks(lametric_icon_uri_template.expand(icon=icon))
    filetype = mimetypes.guess_extension(headers["content-type"])
    filename = f"{icon}{filetype}"
    for chunk in chunker:
        bo.write(chunk)
    return filename, bo

if __name__ == "__main__":
    filename, bo = get_lametric_icon(66)
    print(f"{filename=}")