import argparse

from awtrix_files.list import list_icons


parser = argparse.ArgumentParser(
    prog="awtrix_files",
    description="Manage AWTRIX 3 device files.",
)

parser.add_argument("host", help="the hostname for the awtrix device")

args = parser.parse_args()


body = list_icons(args.host)

print(body)
