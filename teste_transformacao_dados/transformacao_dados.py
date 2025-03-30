import pdfplumber
import pandas as pd
from pathlib import Path
import zipfile

def extrair_e_salvar_csv(caminho_pdf):
    diretorio_atual = Path(caminho_pdf).parent
    diretorio_saida = diretorio_atual.parent
    caminho_csv = diretorio_saida / "tabelas_extraidas.csv"
    
    todas_as_tabelas = []
    
    with pdfplumber.open(caminho_pdf) as pdf:
        for i, pagina in enumerate(pdf.pages[2:]):
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                df = pd.DataFrame(tabela[1:], columns=tabela[0])
                todas_as_tabelas.append(df)
    
    if todas_as_tabelas:
        df_final = pd.concat(todas_as_tabelas, ignore_index=True)
        df_final.to_csv(caminho_csv, index=False, encoding='utf-8')
        print(f"CSV salvo em: {caminho_csv}")
        return caminho_csv
    else:
        print("Nenhuma tabela encontrada.")
        return None
    
def substituir_abreviacoes(caminho_csv):
    substituicoes = {"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}
    
    if caminho_csv:
        df = pd.read_csv(caminho_csv)
        df.columns = df.columns.to_series().apply(lambda x: substituicoes.get(x, x))
        df.replace(substituicoes, inplace=True)
        
        caminho_csv_substituido = caminho_csv.parent / "tabelas_extraidas.csv"
        df.to_csv(caminho_csv_substituido, index=False, encoding='utf-8')
        print(f"Substituições feitas e CSV atualizado: {caminho_csv_substituido}")
        return caminho_csv_substituido
    else:
        print("Arquivo CSV não encontrado.")
        return None
    

diretorio_atual = Path(__file__).parent
caminho_pdf = diretorio_atual / "Anexo_I.pdf"


caminho_csv = extrair_e_salvar_csv(caminho_pdf)
substituir_abreviacoes(caminho_csv)
