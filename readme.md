# Correspondência CBO-2002 × COD-PNAD

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?logo=pandas)

Este projeto automatiza o mapeamento entre dois dos principais sistemas de classificação de ocupações do Brasil: a **CBO-2002** (usada em registros administrativos como RAIS e Novo Caged) e o **COD-Domiciliar** (usado pelo IBGE na PNAD Contínua).

A regra central aplicada é direta: **o código COD-PNAD de 4 dígitos equivale ao grupo de base da CBO-2002** (os 4 primeiros dígitos do código CBO de 6 dígitos).

---

##  Estrutura do Projeto

O código foi modularizado seguindo boas práticas de Engenharia de Dados para facilitar a manutenção e escalabilidade:

```text
cbo-pnad-mapper/
├── data/
│   ├── raw/                  # Coloque aqui a base original (cbo2002-ocupacao.csv)
│   └── processed/            # Tabelas geradas (CSV/Excel) ficam aqui
├── src/
│   ├── __init__.py
│   ├── config.py             # Constantes (ex: Grandes Grupos)
│   ├── data_processing.py    # Lógica de transformação com Pandas
│   ├── export.py             # Funções de estilização e exportação
│   └── utils.py              # Classes para buscas na base
├── main.py                   # Ponto de entrada que executa o pipeline
├── requirements.txt          # Lista de pacotes necessários
└── README.md                 # Documentação do projeto