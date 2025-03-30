from pathlib import Path
import pandas as pd
import zipfile
import os

def concatenar_csv_de_zip(zip_path):
    dfs = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for nome_arquivo in zip_ref.namelist():
            with zip_ref.open(nome_arquivo) as arquivo:
                df = pd.read_csv(arquivo, encoding="utf-8", sep=None, engine="python")
                dfs.append(df)
    
    df_final = pd.concat(dfs, ignore_index=True)
    
    return df_final

def extrair_arquivos_zip(zip_path, destino):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destino)
    print(f"Arquivos extraídos para o diretório: {destino}")

def corrigir_virgulas_para_pontos(diretorio):
    for arquivo in Path(diretorio).glob("*.csv"):
        df = pd.read_csv(arquivo, encoding="utf-8", sep=";")
        for col in df.select_dtypes(include=["object"]).columns:
            df[col] = df[col].replace({',': '.'}, regex=True)
        df.to_csv(arquivo, index=False, encoding="utf-8", sep=";")
        print(f"Arquivo corrigido: {arquivo}")

def processar_arquivos():
    diretorio_atual = Path(__file__).parent

    zip_2023 = diretorio_atual / "2023.zip"
    df_2023 = concatenar_csv_de_zip(zip_2023)

    zip_2024 = diretorio_atual / "2024.zip"
    extrair_arquivos_zip(zip_2024, diretorio_atual)
    
    caminho_saida = diretorio_atual / "despesas_2023.csv"
    df_2023.to_csv(caminho_saida, index=False, encoding="utf-8", sep=";")
    print(f"Arquivo concatenado de 2023 salvo em: {caminho_saida}")
    
    corrigir_virgulas_para_pontos(diretorio_atual)
    
processar_arquivos()
