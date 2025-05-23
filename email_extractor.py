import re
import pandas as pd

csv_file_path = './src/patrocinadores_2025.csv'

status_map = {
    'ENVIAR E-MAIL': 'waiting_send',
    'E-MAIL ENVIADO': 'sent'
}

def extrair_emails(texto):
    if pd.isna(texto):
        return []
    padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(padrao_email, texto)

df = pd.read_csv(csv_file_path)

df['CONTATO'] = df['CONTATO'].apply(extrair_emails)

df = df[df['CONTATO'].map(len) > 0]

df['STATUS'] = df['STATUS'].replace(status_map).fillna('other')

columns_to_display = ['NOME DA EMPRESA', 'CONTATO', 'STATUS']
df_filtered = df[columns_to_display]
