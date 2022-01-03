'''SEC Filing
this will systematically access the different 
sec submissions so the included files can be
accessed (10-K, 8-K, 10-Q, etc) 
Using requests and beautiful soup'''

import requests
from bs4 import BeautifulSoup

# the base url where data is found
base_url = r'https://www.sec.gov/Archives/edgar/data'

# the CIK number of the company
# will need to parse the CIK lookup to create a 
# program to solve for unknown CIK's
cik_num = '/' + '1318605' # Goldman Sachs

# create the filing url in json format
filing_url = base_url + cik_num + '/index.json'
#filing_url = 'https://www.sec.gov/Archives/edgar/data/886982/index.json'
# request the url 
content = requests.get(filing_url, headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'})
#print(content) # check server response

decoded_content = content.json()
#print(decoded_content)
filing_num = decoded_content['directory']['item']#[0]['name']
#print(filling_num)
filings = []
for i in filing_num:
    filings.append(i['name'])
    #print(i)
    #print(i['last-modified'],i['name'])
#print(filings)

for i in filings:
    filing = '/' + str(i)
    url = base_url + cik_num + filing + '/index.json'
    decoded = requests.get(url, headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'})
    file = decoded.json()
    file_json = file['directory']['item']
    print(f'Filing {i} :')
    for g in file_json:
        if g['name'] == 'FilingSummary.xml':
            print(g['name'])
