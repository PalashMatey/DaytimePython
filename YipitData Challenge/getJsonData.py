import json, urllib
from pprint import pprint

def collect_data():
    url = "http://oscars.yipitdata.com/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

#Get all the names --> As a test
def parse_data(data_collected):
    movieNameList = []
    names = data_collected['results'][0]['films'][0]['Detail URL']
    print names

collected_data = collect_data()
parse_data(collected_data)
    

