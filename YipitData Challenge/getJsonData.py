#!/usr/local/bin/python
# -- coding: utf-8 --
import json, urllib
from pprint import pprint
import re
def collect_data(url):

    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def parse_data(data_collected):
    
    tableData = []
    movieBudget = []
    lengthOfResults =len(data_collected['results'])

    for i in range(0,lengthOfResults):
        dataList = []
        detailedUrl = data_collected['results'][i]['films'][0]['Detail URL']
        year = data_collected['results'][i]['year']
        title = data_collected['results'][i]['films'][0]['Film']
        try:
            budget = collect_data(detailedUrl)
            budget = budget['Budget']
            movieBudget.append(convert_budget(budget))

        except KeyError:
            budget = '$4 million'
            movieBudget.append(convert_budget(budget))
        dataList.append(year)
        dataList.append(title)
        dataList.append(budget)
        tableData.append(dataList)
        #print 'year -- title -- Budget', year,title,budget
   # for row in tableData:
    #    print("{: >25} {: >25} {: >25}".format(*row))

    print 'Movie budgets are', movieBudget
    #print 'Length of MovieBudget array is',len(movieBudget)

def convert_budget(budget):
    budget = budget.strip()
    #print budget
    #if '$' in budget:
    winMovieBudget = re.findall(r"\$?([1-9]?[0-9,|.]+)",budget)
    #else:
    #    winMovieBudget = re.findall(r"\u00a3([1-9]?[0-9,|.]+)",budget)
    #    print 'Pound actually got executed',winMovieBudget
    return winMovieBudget[0],budget



url = "http://oscars.yipitdata.com/"
collected_data = collect_data(url)
parse_data(collected_data)


