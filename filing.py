'''SEC Filing
this will systematically access the different 
sec submissions so the included files can be
accessed (10-K, 8-K, 10-Q, etc) 
Using requests and beautiful soup'''

import requests
from bs4 import BeautifulSoup

# the base url where data is found
base_url = r'https://www.sec.gov/Archives/edgar/data'

'''the CIK number of the company
will need to parse the CIK lookup to create a 
program to solve for unknown CIK's'''
cik = '1318605'
cik_num = '/' + '1318605' # Goldman Sachs

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
            sum_url = base_url + cik_num + '/' + i + '/'
            summary_loc.append(sum_url)
            #print (sum_url + 'FilingSummary.xml')

print('Number of Summaries: ' + str(len(summary_loc)))

'''iterate through the summary locations to parse the urls to each 
from filing summary to then find financial reports'''
url_list = []

for x in summary_loc:
    lxml = requests.get(x + 'FilingSummary.xml').content
    #print(x + 'FilingSummary.xml')
    soup = BeautifulSoup(lxml, 'lxml')
    reports = soup.find('MyReports')
    cik_ = {}
    for i, r in enumerate(reports.find_all('Report')[:-1]):
        cik_['cik'] = {}
        cik_['cik']['num'] = cik
        cik_['cik']['url'] = x + r.HtmlFileName.txt
        cik_['cik']['shortname'] = r.ShortName.txt
    url_list.append(cik_)
        
print(url_list)

'''accession number -8:-7 will return the 2 digit year'''