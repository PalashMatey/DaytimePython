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
    #print '\t\t\t\t   Year \t\t\t\t\tTitle \t\t\t\t Budget'
    dataList = ['Year','Title','Budget']
    tableData.append(dataList)
    for i in range(0,lengthOfResults):
        dataList = []
        detailedUrl = data_collected['results'][i]['films'][0]['Detail URL']
        year = data_collected['results'][i]['year']
        title = data_collected['results'][i]['films'][0]['Film']
        try:
            budget = collect_data(detailedUrl)
            budget = budget['Budget']
            budget = convert_budget(budget)
            movieBudget.append(budget)

        except KeyError:
            budget = "US$1 million"
            budget = convert_budget(budget)
            movieBudget.append(budget)
        dataList.append(year.strip()[:4])
        dataList.append(title.strip())
        dataList.append('$' + str(budget).strip())
        tableData.append(dataList)
        #print 'year -- title -- Budget', year,title,budget
    for row in tableData:
        print("{: >43} {: >43} {: >43}".format(*row))
        #print ' %s \t\t %s \t\t\t\t\t\t $%s ' %(year.strip()[:4],title.strip(),str(budget).strip())
   
    print 'Movie Budgets are',movieBudget
    find_average(movieBudget)
    

def convert_budget(budget):
    budget = budget.strip()
    
    if '$' in budget:
        winMovieBudget = re.findall(r"\$?([0-9]?[0-9,|.]+)",budget)
        return process_budget(winMovieBudget[0], True)
    else:
        winMovieBudget = re.findall(r"\$?([0-9]?[0-9,|.]+)",budget)
        return process_budget(winMovieBudget[0],False)
    

def find_average(movieBudgets):

    avg = sum(movieBudgets)/float(len(movieBudgets))
    print 'The average budget of these movies is', avg
    print 'In millions the average budget is ', avg / 1000000

def process_budget(winMovieBudget , flag):
    if flag == True:
    
        if ',' in winMovieBudget:
            winMovieBudget = winMovieBudget.replace(',','')
            return float(winMovieBudget)
        if '.' in winMovieBudget:
            winMovieBudget = float(winMovieBudget) * 1000000
            return winMovieBudget
        else:
            return float(winMovieBudget) * 1000000
    else:
        if ',' in winMovieBudget:
            winMovieBudget = winMovieBudget.replace(',','')
            
            return float(winMovieBudget) * 1.27
        if '.' in winMovieBudget:
            winMovieBudget = float(winMovieBudget) * 1000000 *1.27
            return winMovieBudget
        else:
            return float(winMovieBudget) * 1000000 * 1.27


url = "http://oscars.yipitdata.com/"
collected_data = collect_data(url)
parse_data(collected_data)


