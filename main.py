import os
from pathlib import Path
from src.config import DATA_RAW_DIR, DATA_PROCESSED_DIR
from src.data_processing import (
    load_cbo_data, 
    load_cod_oficial, 
    build_hierarchy, 
    build_correspondence_table
)
from src.export import export_to_csv, export_to_excel

def main():
    DATA_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    
    input_file = DATA_RAW_DIR / 'cbo2002-ocupacao.csv'
    arquivo_cod_oficial = DATA_RAW_DIR / 'CBODomicilar.xlsx - Estrutura CBO-Dom.csv'
    
    csv_output = DATA_PROCESSED_DIR / 'cbo_com_cod_pnad.csv'
    excel_output = DATA_PROCESSED_DIR / 'correspondencia_COD_x_CBO.xlsx'

    if not input_file.exists():
        print(f"Erro: cbo2002-ocupacao.csv nao encontrado.")
        return

    cbo_raw = load_cbo_data(input_file)
    cbo_hierarquia = build_hierarchy(cbo_raw)

    cod_oficial = None
    if arquivo_cod_oficial.exists():
        try:
            cod_oficial = load_cod_oficial(arquivo_cod_oficial)
        except Exception:
            pass

    correspondencia = build_correspondence_table(cbo_hierarquia, cod_oficial)

    export_to_csv(cbo_hierarquia, csv_output)
    export_to_excel(cbo_hierarquia, correspondencia, excel_output)
    
    print("Sucesso!")

if __name__ == '__main__':
    main()