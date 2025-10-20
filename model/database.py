import psycopg2 as psy
from psycopg2 import Error
import logging

logging.basicConfig(
    filename='model.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


RED = '\x1b[1:31'
RESET = '\x1b[0m'

class Database:
    conexao = None

    @staticmethod
    def obter_conexao():
        if Database.conexao is None:
            try:

                Database.conexao = psy.connect(
                        user = 'postgres',
                        password = 'marcos28',
                        host = 'localhost',
                        dbname = 'sistema_financeiro'
                    )
                logging.info(f'SUCESSO: Conexão realizada com sucesso.' )

            except Error as e:
                Database.conexao = None
                logging.error(f'ERRO: {e}.')
        return Database.conexao
            
