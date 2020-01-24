from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request

f = open("sites.csv", 'r')
for i in f:
    try:
        print(BeautifulSoup(urllib.request.urlopen(i), 'html.parser').title.string)
    except: print("error")
print("de")

