from bs4 import BeautifulSoup
import requests

#objeto site recebendo o conteúdo da requisição http do site
site = requests.get("http://fiepe.org.br/").content

#objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

#tranforma o html em string
#print(soup.prettify())

noticia = soup.find("h3")
print(noticia.string)