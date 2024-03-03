# this script applies the class Scraper to your link and saves the
# result as a csv-file

import traceback
from settings import url
from scrape_rbc_articles import Scraper


try:

    scraper = Scraper()

    links = scraper.scrape_links(url)

    df_articles = scraper.scrape_all(links)

    df_articles.to_csv('scraped_articles.csv')

except Exception as e:

    print(e)
    print(traceback.format_exc())
