#Importando as bibliotecas necessárias
import requests     
from bs4 import BeautifulSoup
import os 
from urllib.parse import urljoin 
import zipfile 

#Criando a função para identificar os links pdf do site.
def obter_links_pdfs(url):
    try:
        #Fazendo uma requisição para obter o conteúdo da página
        pagina_pdf = requests.get(url)
        pagina_pdf.raise_for_status()  #Verifica se a requisição foi bem-sucedida
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar: {e}")
        return []
    
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


def baixar_e_compactar_pdfs(links_pdfs):
    # Verifica se não há links PDF encontrados
    if not links_pdfs:
        print("Nenhum link de PDF encontrado.")
        return
    
    zip_filename = "anexos_pdfs.zip"
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for link_pdf in links_pdfs:
            try:
                response = requests.get(link_pdf)
                response.raise_for_status()  # Verifica se o download foi bem-sucedido
                
                # Mantém o nome do arquivo original
                nome_pdf = os.path.basename(link_pdf)
                
                # Adicionando o conteúdo do PDF ao arquivo ZIP e tratamento de erro
                zipf.writestr(nome_pdf, response.content)
                print(f"Arquivo {nome_pdf} adicionado ao zip.")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao baixar o arquivo {link_pdf}: {e}")

    print(f"Arquivos PDF foram baixados e compactados em: {zip_filename}")

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
links_pdfs = obter_links_pdfs(url)
baixar_e_compactar_pdfs(links_pdfs) 