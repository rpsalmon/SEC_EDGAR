'''SEC Filing
this will systematically access the different 
sec submissions so the included files can be
accessed (10-K, 8-K, 10-Q, etc) 
Using requests and beautiful soup'''

import requests
from bs4 import BeautifulSoup

# function to easily make url's
def make_url(root, comp):
    url = root

    for i in comp:
        url = f'{url}/{i}'
    return url

# the base url where data is found
base_url = r'https://www.sec.gov/Archives/edgar/data'

# create a progra that will ask for the ticker and retrieve the cik
ticker = 'RIVN'

'''the CIK number of the company
will need to parse the CIK lookup to create a 
program to solve for unknown CIK's'''
cik = '1559720'
cik_num = '/' + '1559720' # RIVIAN AUTO

'''create the filing url request and decode in json format'''
filing_url = base_url + cik_num + '/index.json'
#filing_url = 'https://www.sec.gov/Archives/edgar/data/886982/index.json'

content = requests.get(filing_url, headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'})
#print(content) # check server response

decoded_content = content.json()
#print(decoded_content)
filing_num = decoded_content['directory']['item']#[0]['name']
#print(filling_num)

'''iterate through the filing numbers in the json appending 
to a list to access later'''
filings = []

for i in filing_num:
    filings.append(i['name'])
    #print(i)
    #print(i['last-modified'],i['name'])

print('Number of Records: ' + str(len(filings)))

'''iterate through the filing numbers and creating the url to 
index the next level down into json
then check the name of each document in the filing folder to 
identify folders with financial reporting included using FilingSummary.xml'''
summary_loc = []

for i in filings:
    filing = '/' + str(i)
    url = base_url + cik_num + filing + '/index.json'
    decoded = requests.get(url, headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'})
    file = decoded.json()
    file_json = file['directory']['item']
    #print(f'Filing {i} :')
    for g in file_json:
        if g['name'] == 'FilingSummary.xml':
            #print(base_url + cik_num + '/' + i + '/' + g['name'])
            summary_url = base_url + cik_num + '/' + i + '/'
            summary_loc.append(summary_url)
            #print (summary_url + 'FilingSummary.xml')

print('Number of Summaries: ' + str(len(summary_loc)))

'''iterate through the summary locations to parse the urls to each 
from filing summary to then find financial reports'''
report_list = []

cik_ = {}
cik_[ticker] = {}

for x in summary_loc:
    lxml = requests.get(x + 'FilingSummary.xml', headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'}).content
    #print(x + 'FilingSummary.xml')
    soup = BeautifulSoup(lxml, 'xml')
    reports = soup.find('MyReports')
    #print(reports)

    for r in reports.find_all('Report')[:-1]:
        cik_[ticker]['cik'] = cik
        cik_[ticker]['url'] = x + str(r.HtmlFileName.text)
        cik_[ticker]['shortname'] = str(r.ShortName.text)
    report_list.append(cik_)
        
print(report_list)

'''accession number -8:-7 will return the 2 digit year'''

