import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_dict = {}

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find("div",class_="content_title").text
    news_title = news_title.strip()

    news_p = soup.find("div",class_="rollover_description_inner").text
    news_p = news_p.strip()

    url = "https://space-facts.com/mars/"
    df = pd.read_html(url)
    mars_df = df[0]
    mars_facts = mars_df.to_html()

    

    mars_dict["title"] = news_title
    mars_dict["news_p"] = news_p
    mars_dict["mars_facts"] = mars_facts
    return mars_dict