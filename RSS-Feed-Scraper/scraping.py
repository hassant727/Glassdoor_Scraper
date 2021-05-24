import requests
from bs4 import BeautifulSoup

def hackernews_rss('https://news.ycombinator.com/rss'):
	try:
		r = requests.get()
		return print('The scraping job suceeded: ', r.status_code)
	except Exceptio as e:
		print('The scraping job failed. See exception: ')
		print(e)

print('Starting Scrpaing')
hackernews_rss()
print('Finished Scraping')


