import pandas as pd
from sqlalchemy import create_engine
import sys

MYSQL_HOST = "localhost"
MYSQL_DB = "fonte_db_mysql"
MYSQL_USER = "root"
MYSQL_PASS = ""


PG_HOST = "localhost"
PG_PORT = "5432"
PG_DB = "teste_db"
PG_USER = "postgres"
PG_PASS = "password"

try:
    print("Iniciado o processo...")

    mysql_conn_str = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DB}"
    mysql_engine = create_engine(mysql_conn_str)
    print("Primeira engine criada.")

    pg_conn_str = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    pg_engine = create_engine(pg_conn_str)
    print("Segunda engine criada")


    query = "SELECT id, produto FROM dados_fonte LIMIT 10;"
    print(f"Executando query na fonte: {query}")

    df = pd.read_sql(query, mysql_engine)

    print("\n--- Dados Coletados ---")
    print(df)
    print("------------------------\n")

    nome_tabela_destino = "copia_pandas_produtos"

    print(f"Iniciando carga para a tabela '{nome_tabela_destino}' no PostgreSQL...")

    df.to_sql(
            nome_tabela_destino,
            pg_engine,
            if_exists='replace',



            index=False

        )

    print("Carga de dados concluída com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro durante o processo de ETL: {e}", file=sys.stderr)

finally:

    print("Processo finalizado.")