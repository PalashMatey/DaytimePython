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
    print 'Year \t\t  Title \t\t Budget'
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
            budget = "US$1 million"
            movieBudget.append(convert_budget(budget))
        # dataList.append(year)
        # dataList.append(title)
        # dataList.append(budget)
        # tableData.append(dataList)
        print ' %s \t\t %s \t\t %s ' %(year.strip(''),title.lstrip(''),budget.lstrip())
    # for row in tableData:
    #     try:
    #         print("{: >25} {: >25} {: >25}".format(*row))
    #     except UnicodeDecodeError:
    #         print row[0],row[1],row[2]

    
    print 'Movie Budgets are',movieBudget
    #print 'Length of MovieBudget array is',len(movieBudget)

def convert_budget(budget):
    budget = budget.strip()
    #print budget
    #if '$' in budget:
    winMovieBudget = re.findall(r"\$?([1-9]?[0-9,|.]+)",budget)
    #else:
    #    winMovieBudget = re.findall(r"\u00a3([1-9]?[0-9,|.]+)",budget)
    #    print 'Pound actually got executed',winMovieBudget
    
    if ',' in winMovieBudget[0]:
        winMovieBudget = winMovieBudget[0].replace(',','')
        return float(winMovieBudget)
    if '.' in winMovieBudget[0]:
        winMovieBudget = float(winMovieBudget[0]) * 1000000
        return winMovieBudget
    else:
        return float(winMovieBudget[0]) * 1000000



url = "http://oscars.yipitdata.com/"
collected_data = collect_data(url)
parse_data(collected_data)


