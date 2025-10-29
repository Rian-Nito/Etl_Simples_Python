#🚀 Pipeline de ETL Simples: MySQL para PostgreSQL com Python
Este é um projeto de demonstração que implementa um script simples de ETL (Extract, Transform, Load) para migrar dados de um banco de dados MySQL para um banco de dados PostgreSQL utilizando Python, Pandas e SQLAlchemy.

Este script foi criado para demonstrar a facilidade com que o Pandas e o SQLAlchemy podem ser usados para criar "engines" de conexão e mover dados entre diferentes sistemas de gerenciamento de bancos de dados (SGBDs).

✨ Funcionalidades
Extração (Extract): Conecta-se a um banco MySQL e extrai dados de uma tabela específica usando uma query SQL.

Carga (Load): Conecta-se a um banco PostgreSQL e carrega os dados extraídos em uma nova tabela.

Segurança: Utiliza variáveis de ambiente (via arquivo .env) para armazenar credenciais de banco de dados, seguindo as melhores práticas de segurança.

Eficiência: Usa o método to_sql() do Pandas para uma inserção de dados otimizada.

🛠️ Tecnologias Utilizadas
Python 3.x

Pandas: Para manipulação de dados em DataFrames (read_sql, to_sql).

SQLAlchemy: Para criar as "engines" de conexão com os bancos de dados.

mysql-connector-python: Driver para conexão com o MySQL.

psycopg2-binary: Driver para conexão com o PostgreSQL.

python-dotenv: Para carregar as variáveis de ambiente do arquivo .env.

⚙️ Pré-requisitos
Antes de começar, você precisará ter:

Python 3.7+ instalado.

Acesso a um servidor MySQL (com um banco de dados e uma tabela fonte).

Acesso a um servidor PostgreSQL (com um banco de dados de destino).

O Git (para clonar o repositório).

🚀 Como Usar
Siga os passos abaixo para executar o projeto localmente.

1. Clone o Repositório
Bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
2. Crie e Ative um Ambiente Virtual
É uma boa prática usar um ambiente virtual para gerenciar as dependências.

Bash

# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
3. Crie o requirements.txt
Crie um arquivo chamado requirements.txt na raiz do projeto com o seguinte conteúdo:

Plaintext

pandas
SQLAlchemy
mysql-connector-python
psycopg2-binary
python-dotenv
4. Instale as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:

Bash

pip install -r requirements.txt
5. Configure as Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto. Ele NÃO deve ser enviado para o GitHub. Copie o conteúdo abaixo e preencha com suas credenciais:

Ini, TOML

# --- Configurações do Banco Fonte (MySQL) ---
MYSQL_USER=seu_usuario_mysql
MYSQL_PASS=sua_senha_mysql
MYSQL_HOST=localhost
MYSQL_DB=seu_banco_mysql

# --- Configurações do Banco Destino (PostgreSQL) ---
PG_USER=seu_usuario_postgres
PG_PASS=sua_senha_postgres
PG_HOST=localhost
PG_PORT=5432
PG_DB=seu_banco_postgres
6. Prepare o Banco de Dados Fonte
Certifique-se de que seu banco MySQL tenha a tabela fonte (dados_fonte, como no exemplo) e que ela contenha alguns dados para a extração.

7. Execute o Script
Finalmente, execute o script Python (ajuste o nome do arquivo se o seu for diferente de teste_etl_pandas.py):

Bash

python teste_etl_pandas.py
Você deverá ver no seu console uma saída similar a esta:

Iniciado o processo...
Primeira engine criada.
Segunda engine criada
Executando query na fonte: SELECT id, produto FROM dados_fonte LIMIT 10;
--- Dados Coletados ---
   id           produto
0   1   Notebook Gamer
1   2  Teclado Mecânico
2   3     Mouse Óptico
-----------------------
Iniciando carga para a tabela 'copia_pandas_produtos' no PostgreSQL...
Carga de dados concluída com sucesso!
Processo finalizado.
👨‍💻 Autor
[Seu Nome]

LinkedIn: https://www.linkedin.com/in/seu-perfil/

GitHub: https://github.com/seu-usuario
