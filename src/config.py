import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"

GRANDES_GRUPOS = {
    '0': 'Forças Armadas, Policiais e Bombeiros Militares',
    '1': 'Membros superiores do poder público, dirigentes de organizações de interesse público e de empresas e gerentes',
    '2': 'Profissionais das ciências e das artes',
    '3': 'Técnicos de nível médio',
    '4': 'Trabalhadores de serviços administrativos',
    '5': 'Trabalhadores dos serviços, vendedores do comércio em lojas e mercados',
    '6': 'Trabalhadores agropecuários, florestais, da caça e pesca',
    '7': 'Trabalhadores da produção de bens e serviços industriais (Grupo I)',
    '8': 'Trabalhadores da produção de bens e serviços industriais (Grupo II)',
    '9': 'Trabalhadores em serviços de reparação e manutenção',
}
