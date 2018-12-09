from bs4 import BeautifulSoup
import requests
r = requests.get("http://python.org")
data=r.content
soup = BeautifulSoup(data,'html.parser')
#print(soup.children[2])
#for link in soup.find_all('a'):
#   print(link.get('href'))
#Beautiful4 is used
for link in soup.find_all('a',class_="jump-to-menu"):
     print(link.get('href'))#should return the href in html href whose class_=jump-to-menu

#a framework for webscrapping using scrapy
