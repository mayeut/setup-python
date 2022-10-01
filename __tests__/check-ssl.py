import ssl
import sys

if sys.version_info[0] == 2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

response = urlopen("https://raw.githubusercontent.com/actions/setup-python/v4/.gitattributes")
data = response.read()
assert len(data) == 61, len(data)
