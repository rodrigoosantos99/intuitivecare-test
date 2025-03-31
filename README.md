# Teste de Nivelamento - Intuitive Care

Este repositório contém os scripts desenvolvidos para o teste de nivelamento da Intuitive Care. Foram realizados três testes:

1. **Web Scraping**: Identifica, Extrai, e Realiza download de PDF e o comprimi em .zip
2. **Transformação e Manipulação de Dados**: Processamento e tratamento de tabelas extraídas de um PDF.
3. **Banco de Dados**: Processamento e armazenamento de dados em um banco PostgreSQL.

Antes de tudo, instale os requisitos através do arquivo da pasta raiz, requirements.txt

Instale usando o seguinte comando no bash:
pip install -r requirements.txt
---

## 1. Web Scraping

O script `web_scraping.py` realiza o seguinte fluxo:
- Acessa a URL: [ANS - Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos).
- Extrai os links de arquivos PDF presentes na página.
- Filtra apenas os arquivos cujo nome contenha "anexo".
- Baixa e compacta os PDFs encontrados em um arquivo `anexos_pdfs.zip`.

### Como Executar
```bash
python web_scraping/script_scraping.py
```
Basta abrir no editor de usa preferência e executar o script
---

## 2. Transformação e Manipulação de Dados

O script `transformacao_dados.py` realiza as seguintes etapas:
- Extrai tabelas de um arquivo PDF `Anexo_I.pdf`.
- Salva os dados extraídos em `tabelas_extraidas.csv`.
- Realiza substituição de abreviações.
- Compacta o CSV final em `Teste_Rodrigo.zip`.

### Como Executar
```bash
python transformacao_dados/transforcamao_dados.py
```
Basta abrir no editor de usa preferência e executar o script
---

## 3. Banco de Dados

A pasta `teste_banco_dados` contém os scripts para a criação e preenchimento do banco de dados PostgreSQL.

### 3.1. Preparar os arquivos CSV
O script `preparar_csv.py`:
- Extrai e concatena arquivos CSV de `2023.zip` e `2024.zip`.
- Realiza correção de formatos numéricos.

### 3.2. Criar o Banco de Dados e as Tabelas

Acesse o **pgAdmin4** e execute os seguintes comandos SQL:

1. **Criar o Banco de Dados**

CREATE DATABASE contabilidade;


2. **Criar as Tabelas**
Abra o banco `contabilidade` e execute:
criar_tabelas.sql

3. **Importar os Arquivos CSV**
Crie manualmente a pasta `C:\PostgreSQL\Uploads\` e copie os arquivos CSV gerados pelo script `preparar_csv.py` para essa pasta.

Depois, execute:
importar_csv.sql

### 3.3. Consultas Analíticas

1. **Empresas que mais gastaram nos últimos 3 meses**
Abra o query tool do pgadmin4 e execute o seguinte script sql:
despesas_ultimo_trimestre.sql

2. **Empresas que mais gastaram no último ano**
Abra o query tool do pgadmin4 e execute o seguinte script sql:
despesas_ultimo_ano.sql

---

