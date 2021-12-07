from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests
import sys
import subprocess
from bs4 import BeautifulSoup
import pdb


movie_name= input("Enter the movie name please ")
print (f"searching for {movie_name}")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome("driver.exe",options=chrome_options)
driver.get(f"https://thepiratebay.org/search.php?q={movie_name}&all=on&search=Pirate+Search&page=0&orderby=[]")
html_list = driver.find_element_by_id("torrents")
items = html_list.find_elements_by_tag_name("li")


for item in items:
    text = item.text
    print(text)
pdb.set_trace()