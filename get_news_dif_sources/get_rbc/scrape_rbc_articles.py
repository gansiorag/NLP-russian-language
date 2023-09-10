import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class Scraper():


	# This program scrapes links of articles from RBC website (search)
	# First you have to go to https://www.rbc.ru/search/, choose the keywords and dates you are looking for
	# Or just use https://www.rbc.ru/search/ if you just want the latest news
	# And then replace the link in the main script (main_rbc.py)

	def scrape_links(self, url):

		scroll_pause_time = 1

		driver = webdriver.Firefox()
		driver.get(url)
		driver.maximize_window()
		links = []

		#measure scroll height

		last_height = driver.execute_script("return document.documentElement.scrollHeight")
		while True:

		    # Scroll down to bottom

			driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

		    # Wait to load page

			time.sleep(scroll_pause_time)

		    # Calculate new scroll height and compare with last scroll height

			new_height = driver.execute_script("return document.documentElement.scrollHeight")
			if new_height == last_height:
				print("break")
				break

			last_height = new_height

			#Get html of the scrolled page

			html = driver.page_source
			html = BeautifulSoup(html, "lxml")
			articles = html.find_all('div', {'class': 'search-item js-search-item'})
			previous_list = ''

			#get all links from the html

			for article in articles:
				ankor_list = article.findChildren('a')

				if ankor_list != previous_list:

					previous_url = ''
					for ankor in ankor_list:
					    url = ankor.get('href')
					    if url != previous_url:
						    links.append(url)
					    previous_url = url
					    #print(url)
				previous_list = ankor_list

		driver.quit()
		#create a dataframe from the list with links

		final = pd.DataFrame({'links' : links})
		final = final[~final['links'].str.contains('#ws')]

		#drop duplicates
		final = final.drop_duplicates(subset=['links'])
		print(final)

		return final


	
	def scrape_article(self, session, url):

		try:

			req = session.get(url)
			plain_text = req.text
			html = BeautifulSoup(plain_text, "lxml")
			title = html.find('span', {'class': 'js-slide-title'})
			print(title)
			title_final = title.text
			articles = html.find('div', {'class': 'article__text article__text_free'})
			article_text = articles.text

		except Exception as e:
			print(e)
			title_final = ''
			article_text = ''


		return {'title' : title_final, 'text' : article_text}


	
	def scrape_all(self, df):

		links = list(df['links'])
		titles = []
		texts = []
		session = requests.Session()
		for link in links:
			info = self.scrape_article(session, link)
			titles.append(info['title'])
			texts.append(info['text'])


		final = pd.DataFrame({'link' : links, 'title' : titles, 'text' : texts})

		return final

