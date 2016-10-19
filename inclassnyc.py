from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.table.find_all('td')





count = 4
n = []

while count < len(table):
	content = str(table[count])
	content = content.strip('<td>')
	content = content.strip('</')
	content = content.split()
	n.append(content)
	count += 5

print n

# for i in range(len(table)):
# 	neighborhoods.append( table[count] )
# 	count +=5



# print soup.table.find_all('td')