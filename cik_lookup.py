''''CIK business reference
This will pull the most up to date info from SEC for 
Company-CIK information and create a dataframe
to reference and lookup against'''

import requests
import pandas as pd
import re

r = requests.get("https://www.sec.gov/Archives/edgar/cik-lookup-data.txt", headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'})
d_r = r.text
#print(decoded)

col_name = ['Company', 'CIK']
cik_ = d_r.splitlines()
#print(cik_)

cik_set = ()
index_list = []
name_list = []
cik_list = []

for i,l in enumerate(cik_):
    index = i
    name = l[:-12]
    cik = l[-11:-1]
    index_list.append(index)
    name_list.append(name)
    cik_list.append(cik)
#print(cik_dict)

df = pd.DataFrame(list(zip(name_list, cik_list)), index=index_list, columns= col_name)
df['CIK_stripped'] = df['CIK'].str.lstrip('0').astype(int)

#print(df.loc[df['CIK_stripped']=='886982'])
#print('df data types\n', df.dtypes)

t = requests.get('https://www.sec.gov/files/company_tickers_exchange.json', headers={'User-Agent': 'Rpsalmon rpsalmon@gmail.com'})
d_t = t.json()
df1 = pd.DataFrame(d_t['data'], columns=d_t['fields'])
df1.rename(columns={'cik':'CIK_stripped'}, inplace=True)
#print(df1.head())
#print('df1 data types\n', df1.dtypes)

fd = df.merge(df1, left_on='CIK_stripped', right_on='CIK_stripped')
print(fd.loc[fd['ticker'].isin(['NKE','TSLA'])])