import pandas as pd
from src.config import GRANDES_GRUPOS

def load_cbo_data(filepath) -> pd.DataFrame:
    cbo = pd.read_csv(filepath, sep=';', encoding='latin1', dtype=str)
    cbo['CODIGO'] = cbo['CODIGO'].str.strip().str.zfill(6)
    return cbo

def load_cod_oficial(filepath) -> pd.DataFrame:
    cod_df = pd.read_csv(filepath, sep=';', encoding='utf-8', dtype=str)
    cod_df.columns = ['COD_PNAD_4dig', 'TITULO_OFICIAL_COD'] 
    return cod_df

def build_hierarchy(cbo_df: pd.DataFrame) -> pd.DataFrame:
    df = cbo_df.copy()
    df['GRANDE_GRUPO_COD'] = df['CODIGO'].str[0]
    df['GRANDE_GRUPO_NOME'] = df['GRANDE_GRUPO_COD'].map(GRANDES_GRUPOS)
    df['SUBGRUPO_PRINCIPAL_COD'] = df['CODIGO'].str[:2]
    df['SUBGRUPO_COD'] = df['CODIGO'].str[:3]
    df['COD_PNAD'] = df['CODIGO'].str[:4]
    return df

def build_correspondence_table(cbo_hierarquia_df: pd.DataFrame, cod_oficial_df: pd.DataFrame = None) -> pd.DataFrame:
    correspondencia = (
        cbo_hierarquia_df
        .groupby('COD_PNAD')
        .agg(
            GRANDE_GRUPO_COD=('GRANDE_GRUPO_COD', 'first'),
            GRANDE_GRUPO_NOME=('GRANDE_GRUPO_NOME', 'first'),
            SUBGRUPO_PRINCIPAL_COD=('SUBGRUPO_PRINCIPAL_COD', 'first'),
            SUBGRUPO_COD=('SUBGRUPO_COD', 'first'),
            TITULO_REFERENCIA_CBO=('TITULO', 'first'),
            QTD_OCUPACOES_CBO=('CODIGO', 'count'),
            TITULOS_CBO=('TITULO', lambda x: ' | '.join(x)),
            CODIGOS_CBO=('CODIGO', lambda x: ' | '.join(x)),
        )
        .reset_index()
        .rename(columns={'COD_PNAD': 'COD_PNAD_4dig'})
    )
    
    if cod_oficial_df is not None:
        correspondencia = correspondencia.merge(
            cod_oficial_df, 
            on='COD_PNAD_4dig', 
            how='left'
        )
        cols = correspondencia.columns.tolist()
        cols.insert(5, cols.pop(cols.index('TITULO_OFICIAL_COD')))
        correspondencia = correspondencia[cols]

    return correspondencia.sort_values('COD_PNAD_4dig')