#!/usr/bin/python
# 2021-05-08
# By Govand Sinjari
# San Diego, CA, USA
# File: crypto_ftx.py
# Get crypto price from FTX.US
# license           : MIT
# py version        : 2.7

import urllib2, json
import datetime
import time

request = urllib2.Request('https://www.ftx.us/api/markets/doge/usd')
request.add_header('User-agent', 'Firefox')
url = urllib2.urlopen(request)
doge = json.load(url)

req2 = urllib2.Request('https://www.ftx.us/api/markets/btc/usd')
req2.add_header('User-agent', 'Firefox')
url2 = urllib2.urlopen(req2)
btc = json.load(url2)


req3 = urllib2.Request('https://www.ftx.us/api/markets/eth/usd')
req3.add_header('User-agent', 'Firefox')
url3 = urllib2.urlopen(req3)
eth = json.load(url3)

dogech = 100*doge["result"]["changeBod"]
#dogec24h = 100*(doge["result"]["change24h"])/(doge["result"]["price"])

btcch = 100*btc["result"]["changeBod"]
#btcc24h = btc["result"]["change24h"]

#print btcc1h
#print btcc24h

ethch = 100*eth["result"]["changeBod"]
#ethc24h = eth["result"]["change24h"]

#print ethc1h
#print ethc24h


#led = "%s DOGE:$%.3f %.2f%% %.2f%% BTC:$%s ETH:$%s" % (datetime.datetime.now().strftime("%a %Y-%m-%d %I:%M:%S%p %z"), float(doge["result"]["price"]), float(100*(doge["result"]["change1h"])/(doge["result"]["price"])),float(100*(doge["result"]["change24h"])/(doge["result"]["price"])), format(float(btc["result"]["price"]), ",.0f"),format(float(eth["result"]["price"]), ",.0f"))

#led = "%s DOGE:$%.3f %.2f%%  BTC:$%s %.2f%%  ETH:$%s %.2f%%" % (datetime.datetime.now().strftime("%a %Y-%m-%d %I:%M:%S%p %z"), float(doge["result"]["price"]), float(dogech), format(float(btc["result"]["price"]), ",.0f"),float(btcch), format(float(eth["result"]["price"]), ",.0f"),float(ethch))

led = "%s DOGE:$%.3f %.2f%%  BTC:$%s %.2f%%  ETH:$%s %.2f%%" % (datetime.datetime.now().strftime("%a %Y-%m-%d %I:%M:%S%p %z"), float(doge["result"]["price"]), float(dogech), format(float(btc["result"]["price"]), ",.0f"),float(btcch), format(float(eth["result"]["price"]), ",.0f"),float(ethch))

print led
