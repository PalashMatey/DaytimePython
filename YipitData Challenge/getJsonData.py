import json, urllib
from pprint import pprint

url = "http://oscars.yipitdata.com/"
response = urllib.urlopen(url)
data = json.loads(response.read())

