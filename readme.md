```markdown
# 📊 Correspondência CBO-2002 × COD-PNAD (IBGE)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?logo=pandas)
![Openpyxl](https://img.shields.io/badge/Openpyxl-Excel_Export-success?logo=microsoftexcel)

Este projeto automatiza o mapeamento e a compatibilização entre os dois principais sistemas de classificação de ocupações do Brasil: a **CBO-2002** (utilizada pelo Ministério do Trabalho em registros como RAIS e Novo Caged) e o **COD-Domiciliar** (utilizado pelo IBGE em pesquisas como a PNAD Contínua).

## 🎯 O que este projeto faz?

Em análises de dados socioeconômicos, cruzar bases do Governo Federal (MTE) com bases de pesquisa (IBGE) é um desafio constante devido à diferença de granularidade das ocupações. 

Este script resolve esse problema aplicando a regra oficial de correspondência: **o código COD-PNAD (4 dígitos) equivale ao grupo de base da CBO-2002 (os 4 primeiros dígitos do código de 6 dígitos)**. 

Além de fazer o agrupamento hierárquico, o código também cruza os dados com a tabela oficial do IBGE para trazer as nomenclaturas exatas, gerando tabelas "DE-PARA" prontas para uso em bancos de dados ou relatórios.

---

## 🚀 Como Utilizar

### 1. Preparação dos Dados Originais
Antes de rodar o código, você precisa fornecer as bases brutas na pasta de dados (`data/raw/`):
* **Arquivo CBO:** Coloque o arquivo `cbo2002-ocupacao.csv` (padrão MTE, separador `;`, encoding `latin1`).
* **Arquivo IBGE (Opcional, mas recomendado):** Coloque o arquivo `CBODomicilar.xlsx - Estrutura CBO-Dom.csv` para que o script capture os nomes oficiais dos grupos definidos pelo IBGE.

### 2. Instalação das Dependências
Certifique-se de ter o Python instalado. No terminal, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 3. Execução
Rode o script principal para iniciar o processamento (ETL):

```bash
python main.py
```

---

## 📈 Resultados Gerados

Após a execução bem-sucedida, os relatórios finais serão salvos automaticamente na pasta `data/processed/`:

* **`cbo_com_cod_pnad.csv`**: A base detalhada completa. Contém o código original de 6 dígitos, hierarquias e o código COD-PNAD de 4 dígitos correspondente. Ideal para realizar *joins/merges* em Python, SQL ou Power BI.
* **`correspondencia_COD_x_CBO.xlsx`**: Um relatório formatado e estilizado em Excel contendo duas abas:
  1. **COD-PNAD x CBO:** Agrupamento focado nos códigos de 4 dígitos, mostrando o nome oficial do grupo, hierarquias e a lista de todas as ocupações específicas que pertencem a ele.
  2. **CBO-2002 Completa:** Tabela de consulta rápida (DE-PARA) linha a linha.

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal para orquestração.
* **Pandas:** Utilizado para extração, transformação de strings, agrupamento e cruzamento (merge) dos dados.
* **Openpyxl:** Utilizado para a geração do relatório final em Excel, aplicando cores, larguras de colunas, congelamento de painéis e filtros automatizados.
```