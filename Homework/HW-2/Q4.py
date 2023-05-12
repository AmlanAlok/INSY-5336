# import necessary libraries
import requests
from bs4 import BeautifulSoup
import sqlite3

# define dictionaries for commodity symbols and class values for each commodity
commodities = {'gold': 'GC=F', 'crude-oil': 'CL=F', 'silver': 'SI=F'}
class_values = {'gold': 'Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)',
                'crude-oil': 'Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)',
                'silver': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}

# open file to write commodity prices and connect to database
with open('commodity_prices.txt', 'w') as file, sqlite3.connect('CommodityDatabase.db') as con:
    # create table for commodity prices in database
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS CommodityTable (Ticker TEXT, Price REAL)''')

    # loop through each commodity and retrieve its price from Yahoo Finance
    for commodity, symbol in commodities.items():
        url = f'https://finance.yahoo.com/quote/{symbol}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        # extract the price of the commodity from the HTML using the appropriate class value and symbol
        price = soup.find('fin-streamer', {'class': class_values[commodity], 'data-symbol': symbol}).text
        # write the commodity and its price to the file
        file.write(f'{commodity}\t\t{price}\n')
        # insert the commodity and its price into the database
        cur.execute("INSERT INTO CommodityTable VALUES (?, ?)", (commodity, price))
    # commit changes to the database
    con.commit()

# print the rows in the CommodityTable
for row in sqlite3.connect('CommodityDatabase.db').cursor().execute('SELECT * FROM CommodityTable'):
    print(row)
