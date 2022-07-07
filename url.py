headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

url = "https://mercado.carrefour.com.br/"

def search_url(): 
    #cep = input("Please, insert your CEP: ")
    product_searched = input("Search your product: ")
    space_check = product_searched.find(" ")

    if space_check == 0:
        url = "https://mercado.carrefour.com.br/s/"+product_searched+"?map=term"
    
    else: 
        product_searched = product_searched.replace(" ", "%20", space_check)
        url ="https://mercado.carrefour.com.br/s/"+product_searched+"?map=term"

    return url
