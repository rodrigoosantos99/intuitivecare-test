#Importando as bibliotecas necessárias
import requests     #requisições HTTP
from bs4 import BeautifulSoup   #Análise de conteúdo HTML
import os   #Interação com o sistema operacional
from urllib.parse import urljoin    #Manipulação de URLs
import zipfile  #Manipulação de arquivos zip

#Criando a função para identificar os links pdf do site.
def obter_links_pdfs(url):
    try:
        #Fazendo uma requisição para obter o conteúdo da página
        pagina_pdf = requests.get(url)
        pagina_pdf.raise_for_status()  #Verifica se a requisição foi bem-sucedida
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar: {e}")
        return []
    
    #Parse na página
    dados_pagina = BeautifulSoup(pagina_pdf.text, 'html.parser')
    #Encontrando todos os links na página
    todos_links = dados_pagina.find_all('a', href=True)
    
    # Filtra os links de PDFs que contenham "anexo" no nome e terminem com ".pdf"
    links_pdfs = []
    for links in todos_links:
        href = links['href']
        href_lower = href.lower()  # Converte o link para minúsculas uma vez para otimizar
        if 'anexo' in href_lower and href_lower.endswith('.pdf'):
            # Se o link for relativo, converte para absoluto
            href_completo = urljoin(url, href)
            links_pdfs.append(href_completo)

    return links_pdfs