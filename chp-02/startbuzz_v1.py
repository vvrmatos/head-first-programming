#!/usr/bin/env python3

import urllib.request

message = "Pattern not found"
webpage = "https://beans.itcarlow.ie/prices.html"

page = urllib.request.urlopen(webpage)
text = page.read().decode("UTF-8")

print(text)
