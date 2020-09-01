# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import xlrd
import xlwt
import pandas as pd
import schedule
import time
from yahoo_fin.stock_info import*
from datetime import date
import json
import math



#appending stock list
stocklist = []
workbook = xlrd.open_workbook('/Users/samuelpark/Desktop/Web Development/Project_OP/StockData Retrive (Python)/sp250.xlsx')
worksheet = workbook.sheet_by_index(0)
for i in range(0,249):
    stocklist.append(worksheet.cell(i,1).value)


#test
stockname = stocklist[2]
stockinfo = get_quote_table('{}'.format(stockname), dict_result= False)
html = stockinfo.to_html()
print(html)



#information getter runs every hour for companies in the stocklist
#output as a html
def retrivestockinfo():
    today = date.today()
    d = today.strftime("%m/%d/%y")
    for i in range(0,249):
        stockname = stocklist[i]
        stockinfo = get_quote_table('{}'.format(stockname), dict_result= False)
        html = stockinfo.to_html()
        print(html) 

#output info as a string
def retrivestockinfostring():
    today = date.today()
    d = today.strftime("%m/%d/%y")
    for i in range(0,249):
        stockname = stocklist[i]
        stockinfo = get_quote_table('{}'.format(stockname))
        string = json.dumps(stockinfo)
        print(string)

# making func to retrieve a stock quote
def getIndividualQuote(symbol):
    rawQuote = get_live_price(symbol) # returns a long float
    if math.isnan(rawQuote):
        print("invalid symbol")
        # return null (find better way of handling this)
    else:
        truncatedQuote = "%.2f" % rawQuote # truncate after two decimal places
        print(symbol + ' price: $' + truncatedQuote)

getIndividualQuote('AAPL') # test
getIndividualQuote('APL') # testing wrong symbol
        
#schedule.every(1).hour.do(retrivestockinfo)
#while True:
    #schedule.run_pending
    #time.sleep(1)