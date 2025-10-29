import mysql.connector
import psycopg2
import sys

# --- 1. Configurações ---

MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "fonte_db_mysql"
MYSQL_USER = "root"
MYSQL_PASS = ""

PG_HOST = "localhost"
PG_PORT = "5432"
PG_DB = "teste_db"
PG_USER = "postgres"
PG_PASS = "password"

dados_coletados = []

# --- 2. Extração (Conectar e Ler do MySQL) ---
conn_mysql = None
cursor_mysql = None

try:
    print("Conectando")
    conn_mysql = mysql.connector.connect(
        host=MYSQL_HOST,
        database=MYSQL_DB,
        user=MYSQL_USER,
        password=MYSQL_PASS
    )

    if conn_mysql.is_connected():
        print("Conectado ao MySQL com sucesso")

        cursor_mysql = conn_mysql.cursor()

        query = ("SELECT id, produto from dados_fonte;")
        print(f"executando a Query: {query}")

        cursor_mysql.execute(query)

        dados_coletados = cursor_mysql.fetchall()

        print(f"Dados coletados: {dados_coletados}")

except mysql.connector.Error as e:
    print(f"Erro ao conectar ou ler do MySQL: {e}", file=sys.stderr)

finally:
    if cursor_mysql:
        cursor_mysql.close()
    if conn_mysql and conn_mysql.is_connected():
        conn_mysql.close()
        print("Conexão MySql Fechada")

# --- 3. Carga (Conectar e Escrever no PostgreSQL) ---
if not dados_coletados:
    print("\nNenhum dado foi coletado da fonte. Encerrando.")
else:
    print(f"\nIniciando carga de {len(dados_coletados)} registros para o PostgreSQL...")

    conn_pg = None
    cursor_pg = None

    try:
        conn_pg = psycopg2.connect(
            dbname=PG_DB,
            user=PG_USER,
            password=PG_PASS,
            host=PG_HOST,
        )
        print("Conetado ao PostgreSQL!")

        cursor_pg = conn_pg.cursor()

        insert_query = "INSERT INTO copia_produtos (id, produto) VALUES (%s, %s);"

        for dados in dados_coletados:
            print(f"Inserindo: {dados}")
            cursor_pg.execute(insert_query, dados)

            conn_pg.commit()
            print("Commit realizado! Dados salvos no PostgreSQL.")

    except psycopg2.Error as e:
        print(f"Erro ao conectar ou escrever no PostgreSQL: {e}", file=sys.stderr)
        if conn_pg:
            conn_pg.rollback()
            print("Rollback realizado.")

    finally:
        if cursor_pg:
            cursor_pg.close()
        if conn_pg:
            conn_pg.close()
            print("Conexão PostgreSQL fechada.")