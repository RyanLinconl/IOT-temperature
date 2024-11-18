import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão com o PostgreSQL
DATABASE_URI = 'postgresql://postgres:coio1234@localhost:5432/postgres'
engine = create_engine(DATABASE_URI)

# Carregar e limpar os dados do CSV
file_path = 'IOT-temp.csv'
data = pd.read_csv(file_path)

# Remover duplicatas
data_cleaned = data.drop_duplicates(subset=['id'])

# Converter 'noted_date' para datetime
data_cleaned['noted_date'] = pd.to_datetime(data_cleaned['noted_date'], errors='coerce', format='%d-%m-%Y %H:%M')

# Remover valores nulos
data_cleaned = data_cleaned.dropna()

# Enviar os dados limpos para o banco de dados
data_cleaned.to_sql('temperature_readings', engine, if_exists='replace', index=False)
print("Dados inseridos com sucesso!")
