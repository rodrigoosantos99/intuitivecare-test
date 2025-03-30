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
    
# Caminho do PDF
diretorio_atual = Path(__file__).parent
caminho_pdf = diretorio_atual / "Anexo_I.pdf"

# Chamando as funções
caminho_csv = extrair_e_salvar_csv(caminho_pdf)
