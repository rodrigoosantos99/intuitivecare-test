from pathlib import Path
import pandas as pd
import zipfile

def concatenar_csv_de_zips(arquivos_zip):
    dfs = []

    for zip_path in arquivos_zip:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for nome_arquivo in zip_ref.namelist():
                with zip_ref.open(nome_arquivo) as arquivo:
                    df = pd.read_csv(arquivo, encoding="utf-8", sep=None, engine="python")
                    dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)
    caminho_saida = diretorio_atual/"despesas_2023_2024.csv"
    df_final.to_csv(caminho_saida, index=False, encoding="utf-8")

    print(f"Arquivo consolidado salvo em: {caminho_saida}")


diretorio_atual = Path(__file__).parent

zip_arquivos = [diretorio_atual/"2023.zip", diretorio_atual/"2024.zip"]
concatenar_csv_de_zips(zip_arquivos)



