from bs4 import BeautifulSoup
import requests
import pandas

page = requests.get("https://www.marketwatch.com/story/aptiv-plc-stock-outperforms-competitors-on-strong-trading-day-01621975060-4b938fc52cda")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#print(list(soup.children))
print([type(item) for item in list(soup.children)])

html = list(soup.children)[2]
print(list(html.children))