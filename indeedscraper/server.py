from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://www.indeed.com/jobs?q=react+developer&l=Remote&sort=date&vjk=e1e2096e28d72108"
page = urlopen(url)
html = page.read().decode("utf-8")


print(html)