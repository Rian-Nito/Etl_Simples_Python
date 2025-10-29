import psycopg2
import sys

# --- 1. Configurações ---

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "teste_db"
DB_USER = "postgres"
DB_PASS = "password"

conn = None
cursor = None

try:
    # --- 2. Conecta ao teste_db ---
    print(f"Tentando conectar ao banco '{DB_NAME} em {DB_HOST} ")

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    print("Conexão bem-sucedida")

    # --- 3. Cria um "cursor" ---
    cursor = conn.cursor()

    # --- 4. Executa um SELECT * FROM usuarios; ---
    query = "SELECT id, produto FROM copia_produtos;"
    print(f"Executando query: {query}")

    cursor.execute(query)

    # --- 5. Pega os resultados (cursor.fetchall()) ---
    registros = cursor.fetchall()

    print("--- Resultados Encontrados ---")
    if not registros:
        print("Nenhum usuário encontrado na tabela.")
    else:
        # --- 6. Mostra os registro e um loop ---
        for registro in registros:
            print(f"ID: {registro[0]}, Nome: {registro[1]}")

    print("------------------------------------\n")
except psycopg2.OperationalError as e:
    print(f"Erro de conexão: {e}", file=sys.stderr)
except Exception as e:
    print(f"Ocorreu um erro: {e}", file=sys.stderr)
finally:
    # --- 7.  Fecha o cursor e a conexão ---
    if cursor:
        cursor.close()
        print("Cursor fechado.")
    if conn:
        conn.close()
        print("Conexão fechada.")