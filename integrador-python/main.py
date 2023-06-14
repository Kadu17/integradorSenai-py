import requests
from bs4 import BeautifulSoup
import pandas as pd

listanome = []
listapreco = []

abaUm = requests.get('http://127.0.0.1:5500/LIMA_AULA2/Produtos.html')
soup = BeautifulSoup(abaUm.content, 'html.parser')

nome = soup.find_all("h1")
prec = soup.find_all("p")

print(nome)
for c in nome:
    c = c.text
    listanome.append(c)


print(prec)
for c in prec:
    c = c.text
    listapreco.append(c)


planilha = {"Tenis": listanome, "Preço": listapreco}
plan = pd.DataFrame(planilha)

plan.to_excel("Web.xlsx")
