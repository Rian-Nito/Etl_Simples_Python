import pandas as pd
from sqlalchemy import create_engine
import sys
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Agente de Coleta teste",
    description="Teste de microserviço para executar"
)

def executar_etl_pandas():
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

        # --- 3. Extração (E) ---

        query = "SELECT id, produto FROM dados_fonte;"
        print(f"Executando query na fonte: {query}")

        df = pd.read_sql(query, mysql_engine)

        print("\n--- Dados Coletados ---")
        print(df)
        print("------------------------\n")

        # --- 4. Transformação (T) ---
            # Nosso projeto não pede, mas aqui você poderia:
            # df['nova_coluna'] = 'Valor Fixo'
            # df['produto'] = df['produto'].str.upper() # Deixar tudo maiúsculo
            # print("Dados transformados:\n", df)

        # --- 5. Carga (L) ---

        nome_tabela_destino = "copia_pandas_produtos"


        print(f"Iniciando carga para a tabela '{nome_tabela_destino}' no PostgreSQL...")

        df.to_sql(
                nome_tabela_destino,       # Nome da tabela que será criada/substituída
                pg_engine,                 # Engine de conexão do destino (PostgreSQL)
                if_exists='replace',       # O que fazer se a tabela já existir:
                                           # 'replace': Apaga a tabela e cria de novo (ótimo para testes)
                                           # 'append': Adiciona os dados no final (bom para produção)
                                           # 'fail': Dá erro (padrão)
                index=False                # IMPORTANTE: Não salva o índice (0, 1, 2...) do pandas
                                           # como uma coluna no banco SQL.
            )

        print("Carga de dados concluída com sucesso!")

        return {"status": "ok", "registros_transferidos": len(df)}

    except Exception as e:
        print(f"Ocorreu um erro durante o processo de ETL: {e}", file=sys.stderr)
        raise HTTPException(
            status_code=500,
            detail=f"Falha no processo de ETL: {e}"
        )

@app.post("/coletar-dados")
def endpoint_coletar_dados():
    print("API: Chamada recebida em /coletar-dados")
    return executar_etl_pandas()

@app.get("/")
def read_root():
    return {"status": "API do Agente de Coleta está online."}

# --- 4. (Opcional) Linha para rodar direto com "python main.py" ---
if __name__ == "__main__":
    print("Iniciando servidor Uvicorn em http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)