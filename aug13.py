"""
40 Singles
"""
import urllib2, requests
from bs4 import BeautifulSoup
from lxml import html


url = 'https://top40weekly.com/1980-all-charts/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
page_req = requests.get(url)
tree = html.fromstring(page_req.text)


"""
with open('whole_result.txt', 'w') as f:
	f.write(str(soup) )
f.close()

page_body = soup.find(class_='page-body')
with open('page_body.txt', 'w') as f:
	f.write(str(page_body) )
f.close()



all_p = soup.find_all('p')
all_p = str(all_p)
with open('all_p.txt', 'w') as f:
	f.write(all_p) 
f.close()

all_p_list = all_p.split(',')
with open('all_p_list.txt', 'w') as f:
	for index, value in enumerate(all_p_list):
		f.write(all_p_list[index] + '\n') 
f.close()
"""

#//*[@id="post-3198"]/div/h2[2]  ---- info for week
#xpath>> //*[@id="post-3198"]/div/p[16] //*[@id="post-3198"]/div/p[18] //*[@id="post-3198"]/div/p[19] ---- info for each 10 songs
week_16=tree.xpath('//*[@id="post-3198"]/div/p[16]/text()')
for i in week_16:
	print(i)
for i in range(1,12):
	x = tree.xpath('//*[@id="post-3198"]/div/h2['+ str(i) + ']/text()')
	print(x)	

