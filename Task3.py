import requests
import pandas as pd
from bs4 import BeautifulSoup

req = requests.get('http://finance.yahoo.com/q/hp?s=GE&a=00&b=2&c=1962&d=03&e=25&f=2016&g=d')
if req.status_code == 200:
    print('requisição bem sucedida')
    content = req.content

s = BeautifulSoup(content, 'html.parser')
tabela = s.find(name='table')

tabela_str = str(tabela)
df = pd.read_html(tabela_str)[0]
print(df)

