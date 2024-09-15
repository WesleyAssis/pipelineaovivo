import psycopg2
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()


# Configurações do banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def testar_conexao():
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        
        # Definir a codificação da conexão
        conn.set_client_encoding('UTF8')
        
        # Fechar a conexão
        conn.close()
        
        print("Conexão bem-sucedida com o banco de dados!")
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


testar_conexao()


print(f"DB_HOST: {DB_HOST}")
print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PASS: {DB_PASS}")