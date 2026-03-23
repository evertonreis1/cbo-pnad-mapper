import os
from pathlib import Path
from src.config import DATA_RAW_DIR, DATA_PROCESSED_DIR
from src.data_processing import load_cbo_data, build_hierarchy, build_correspondence_table
from src.export import export_to_csv, export_to_excel
from src.utils import CBOHelper

def main():
    DATA_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    input_file = DATA_RAW_DIR / 'cbo2002-ocupacao.csv'
    csv_output = DATA_PROCESSED_DIR / 'cbo_com_cod_pnad.csv'
    excel_output = DATA_PROCESSED_DIR / 'correspondencia_COD_x_CBO.xlsx'

    if not input_file.exists():
        print(f"⚠️  Atenção: Coloque o arquivo 'cbo2002-ocupacao.csv' na pasta: {input_file}")
        return

    print("Carregando e processando dados...")
    cbo_raw = load_cbo_data(input_file)
    cbo_hierarquia = build_hierarchy(cbo_raw)
    correspondencia = build_correspondence_table(cbo_hierarquia)

    print("\\nExportando arquivos...")
    export_to_csv(cbo_hierarquia, csv_output)
    export_to_excel(cbo_hierarquia, correspondencia, excel_output)
    print("Sucesso! Arquivos salvos em 'data/processed/'.")

if __name__ == '__main__':
    main()