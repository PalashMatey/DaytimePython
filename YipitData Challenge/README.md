Dependencies: 
•	Python 2.7.10
•	urllib 1.17
•	json 2.0.9
•	re 2.2.1

Instruction to run:	
•	python parseMessyApi.py

The average budget of all the winners is $17226711.39


Assumptions:
•	The first element under films is always the Winner
•	Other than the Pound and Dollar there are no other currencies present
•	1 Pound is 1.27 Dollar
•	Value of missing Budget Fields is taken as 0.0 & Ignored during Average Calculation
•	For a given Range: 16.5-18 million, I have considered the lower bound


Approach:
1.	Converted string data to Json as its easier to access(Thank you for the wonderfully formatted data). 
2.	Picked out the Winners of each year
3.	Followed the ‘Detailed Url’ to get to the Budget and Title (less ambiguous)
4.	Parsed the Budget to return Float Values taking into account Dollar and Pound conversions
5.	All returned Budget Values are in Dollar
6.	Stored all the budget values in an array
7.	Ignored all missing values while calculating average
a.	No trend between previous and past values of budget
b.	No strong correlation between box office earning and budget
c.	Within the same year there was no consistency with movie budget
8.	Used this array to find the average

