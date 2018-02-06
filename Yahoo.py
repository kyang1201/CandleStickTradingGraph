
#Mel    #2/6/2018
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
import warnings
warnings.filterwarnings('ignore')

#Enter the below command to your terminal
#sudo pip install requests
import urllib

#Enter the below command to your terminal 
#sudo pip install BeautifulSoup4
from bs4 import BeautifulSoup as bs

def get_historical_data(name, number_of_days):
    data = []
    url = "https://finance.yahoo.com/quote/" + name + "/history/"
    wp = urllib.urlopen(url)
    rows = bs(wp.read()).findAll('table')[0].tbody.findAll('tr')

    for each_row in rows:
        divs = each_row.findAll('td')
        if divs[1].span.text  != 'Dividend': #Ignore this row in the table
            #I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
            data.append({'Date': divs[0].span.text, 'Open': float(divs[1].span.text.replace(',','')),'High': float(divs[2].span.text.replace(',','')),'Low': float(divs[3].span.text.replace(',','')),'Close':float(divs[4].span.text.replace(',',''))})

    return data[:number_of_days]

#Test
print (get_historical_data('uvxy', 3))







