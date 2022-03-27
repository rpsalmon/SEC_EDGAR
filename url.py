from bs4 import BeautifulSoup
import requests

url = 'www.google.com'
comp = ['flights','index.html','another','and again']

for i in comp:
    url = f'{url}/{i}'

#print(url)
print('/'*75)

ticker = 'AbC'
cik = '12345'
url_list = []

url = 'https://www.sec.gov/Archives/edgar/data/1559720/000155972021000017/FilingSummary.xml'
ur = 'https://www.sec.gov/Archives/edgar/data/1559720/000155972021000017/'
lxml = requests.get(url, headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'}).content
#print(x + 'FilingSummary.xml')
soup = BeautifulSoup(lxml, 'xml')
reports = soup.find('MyReports')
#print(reports.find_all('Report')[0].HtmlFileName.text)
cik_ = {}
cik_[ticker] = []
tic = cik_[ticker] 
#print(reports.find_all('Report')[:-1])

for r in reports.find_all('Report')[:-1]:
    ker = {}
    #ker['num'] = cik
    ker['url'] = ur + str(r.HtmlFileName.text)
    ker['shortname'] = str(r.ShortName.text)
    tic.append(ker)
url_list.append(cik_)
#print(url_list)
#print(len(tic))
#print(url_list[0]['AbC'][52]['shortname'])
#https://www.sec.gov/Archives/edgar/data/1559720/000162828021010389/R55.htm

'''create a loop to iterate through the tickers and return the
titles of the different reports using cik_lookup
for each iteration in the lenght of url_list
for each ticker in the list'''
short = url_list[0]['AbC']
docs = set()

'''this will create a list of all the report titles'''
for i in short:
    docs.add(i['shortname'])
print(len(docs))
print(list(docs))