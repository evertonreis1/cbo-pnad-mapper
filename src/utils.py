import pandas as pd

class CBOHelper:
    def __init__(self, cbo_df: pd.DataFrame, correspondencia_df: pd.DataFrame):
        self.cbo = cbo_df
        self.cbo_para_cod = dict(zip(cbo_df['CODIGO'], cbo_df['COD_PNAD']))
        self.cod_para_nome = dict(zip(correspondencia_df['COD_PNAD_4dig'], correspondencia_df['TITULO_REFERENCIA']))

    def cbo_to_cod(self, codigo_cbo: str) -> dict:
        codigo_cbo = str(codigo_cbo).strip().zfill(6)
        cod = self.cbo_para_cod.get(codigo_cbo)
        if cod:
            return {
                'cbo_6dig': codigo_cbo,
                'cod_pnad_4dig': cod,
                'titulo_cod': self.cod_para_nome.get(cod, ''),
            }
        return {'cbo_6dig': codigo_cbo, 'cod_pnad_4dig': None, 'titulo_cod': 'NÃO ENCONTRADO'}

    def buscar_ocupacao(self, termo: str, por: str = 'titulo') -> pd.DataFrame:
        if por == 'titulo':
            mask = self.cbo['TITULO'].str.contains(termo, case=False, na=False)
        else:
            mask = self.cbo['CODIGO'].str.startswith(str(termo).zfill(4))
        
        resultado = self.cbo.loc[mask, ['CODIGO', 'TITULO', 'COD_PNAD', 'GRANDE_GRUPO_NOME']].copy()
        resultado.columns = ['CBO-2002 (6 dig)', 'Título CBO', 'COD-PNAD (4 dig)', 'Grande Grupo']
        return resultado
