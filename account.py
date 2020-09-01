from yahoo_fin.stock_info import *
from datetime import date
import json
import math
class account():
    def __init__(self, cash, stock):
        self.cash = cash
        self.stock = stock
    def check_balance(self):
        return self.cash
    def check_stock(self):
        return self.stock
    def add_cash(self, amount):
        self.cash = self.cash + amount
        return 'you have successfully add: ${}'.format(amount)
    def buy_stock(self,stock_name,amount):
        try:
            stockprice = self.getIndividualPrice(stock_name)
        except:
            return "Wrong ticker symbol"
        cost = stockprice * amount
        if self.cash >= cost:
            self.cash = self.cash - cost
            self.stock[stock_name]= amount
            return 'you have successfully purchased '+str(amount)+' shares of '+ stock_name
        else:
            return 'Not enough cash, You brokeasss motherfucker'
    def sell_stock(self, stock_name,amount):
        if stock_name in self.stock:
            if self.stock.get(stock_name)>= amount:
                self.stock[stock_name] = self.stock.get(stock_name) - amount
                try:
                    stockprice = self.getIndividualPrice(stock_name)
                except:
                    return "Wrong ticker symbol"
                self.cash = self.cash + amount * stockprice
                return 'you have successfully sold ' + str(amount) +' shares of '+stock_name
            else:
                return 'You dont have enough stock, stupid'
        else:
            return 'You dont have enough stock, stupid'
    def getIndividualPrice(self, symbol):
        rawPrice = get_live_price(symbol) # returns a long float
        strtruncatedPrice = "%.2f" % rawPrice # truncate after two decimal places
        truncatedPrice = float(strtruncatedPrice)
        return truncatedPrice