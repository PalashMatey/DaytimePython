#!/usr/local/bin/python
# -- coding: utf-8 --
import json, urllib
import re

def collect_data(url):
    #Function to collect data from given Url
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def parse_data(data_collected):
    #Main function where each element is parsed
    tableData = []
    movieBudget = []
    lengthOfResults =len(data_collected['results'])
    dataList = ['Year','Title','Budget']
    tableData.append(dataList)
    
    #running through to get details of all the winners
    for i in range(0,lengthOfResults):
        dataList = []
        try:
            detailedUrl = data_collected['results'][i]['films'][0]['Detail URL']
            year = data_collected['results'][i]['year']
        #title present in both 'films'['Film'] and 'Detail Url'. I am using 'Detail Url'' to get 'Title'(Although it takes longer) but seems less ambiguous
            title = collect_data(detailedUrl)
            title = title['Title']
        except KeyError:
            print 'Check for missing data'

        #For some Winners --> Budget Field is missing
        #convert_budget --> parses the Budget Field --> returning Float
        try:
            budget = collect_data(detailedUrl)
            budget = budget['Budget']
            budget = convert_budget(budget)
            movieBudget.append(budget)
        except KeyError:
            #Placeholder Budget Value --> Makes parsing easier
            budget = "US$0 million"
            budget = convert_budget(budget)
            movieBudget.append(budget)

        dataList.append(year.strip()[:4])
        dataList.append(title.strip())
        #Ensure data is correctly displayed in the table when Not Available 
        if budget == 0:
            dataList.append("Not Available")
        dataList.append('$' + str(budget).strip())
        tableData.append(dataList)

    for row in tableData:
        print("{: >48} {: >48} {: >48}".format(*row))

    find_average(movieBudget)
    

def convert_budget(budget):
    budget = budget.strip()
    #There are more than one currencies in the data --> Considering just Dollar and Pound
    #process_budget returns converted value in Dollar
    if '$' in budget:
        winMovieBudget = re.findall(r"\$?([0-9]?[0-9,|.]+)",budget)
        return process_budget(winMovieBudget[0], True)
    else:
        winMovieBudget = re.findall(r"\$?([0-9]?[0-9,|.]+)",budget)
        return process_budget(winMovieBudget[0],False)
    
def process_budget(winMovieBudget , flag):
    PoundtoDollar = 1.27
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
        #conversion rate for pound -> Dollar is currently at 1.27
        if ',' in winMovieBudget:
            winMovieBudget = winMovieBudget.replace(',','')
            return float(winMovieBudget) * PoundtoDollar
        if '.' in winMovieBudget:
            winMovieBudget = float(winMovieBudget) * 1000000 * PoundtoDollar
            return winMovieBudget
        else:
            return float(winMovieBudget) * 1000000 * PoundtoDollar

def find_average(movieBudgets):
    #Decided to ignore 'Not Available Values'
    movieBudgetLength = len(movieBudgets)
    for num in range(0,len(movieBudgets)):
        if movieBudgets[num] == 0:
            movieBudgetLength -= 1

    avg = sum(movieBudgets)/float(movieBudgetLength)
    print 'The average budget of these movies is $%.2f'%(avg)
    


url = "http://oscars.yipitdata.com/"
collected_data = collect_data(url)
parse_data(collected_data)


