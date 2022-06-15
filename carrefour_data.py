from bs4 import BeautifulSoup
import requests
import praticando_plawright

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

url = "https://mercado.carrefour.com.br/"

cep = input("Please, insert your CEP: ")
product_searched = input("Search your product: ")
space_check = product_searched.find(" ")

if space_check == 0:
    url = "https://mercado.carrefour.com.br/s/"+product_searched+"?map=term"
    
else: 
    product_searched = product_searched.replace(" ", "%20", space_check)
    url ="https://mercado.carrefour.com.br/s/"+product_searched+"?map=term"

print(url)

praticando_plawright.StartPlayWirght()

response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content, "html.parser")

#testo = soup.find_all("h1")
print(soup.prettify())

#print(testo)

#print(soup.prettify())


#"div", {"class":"css-1u9y7ms"}