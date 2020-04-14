#!/usr/bin/python3
from urllib.request import urlopen


with urlopen("https://intranet.hbtn.io/status") as response:
   html = response.read()
