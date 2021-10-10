#!/usr/bin/python
# 2021-05-09
# By Govand Sinjari
# San Diego, CA, USA
# File: stock_yahoo
# Get stock & crypto price from Yahoo
# Modified: https://github.com/aiweier1231/stockTicker/blob/master/yahoo.py, Had issue with Cypto info retrieval, change the price line class to find the issue
# license           : MIT
# py version        : 2.7

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
stocks = ['DOGE-USD', 'ETH-USD', 'BTC-USD', 'UAL', 'TSLA', 'ALK', 'COIN', 'ON', 'SPCE', 'EPD']

stz = ''

for stock in stocks:
	try:
		URL = 'https://finance.yahoo.com/quote/' + stock + '/'
		page = requests.get(URL)
		soup = BeautifulSoup(page.text, 'lxml')
#		price = soup.find('div', {'class': "My(6px) Pos(r) smartphone_Mt(6px)"}).find('span').text
		price = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
		change = soup.find('span', {'class': ['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                                  'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)']}).text
		stx = stock + ":$" + price + " " + change + " "
		stz += stx
#		print(stx)
#		if float(change.split(" ")[0]) >= 0:
#			print("[" + Fore.GREEN + change + Style.RESET_ALL + "]")
#		else:
#			print("[" + Fore.RED + change + Style.RESET_ALL + "]")
	except:
		print("An error occurred fetching " + stock)


print(stz)