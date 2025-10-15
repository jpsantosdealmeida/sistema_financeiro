import psycopg2 as psy
from categoria import Categoria

class Database:
    def __init__(self,usuario,senha,host,database):
        self.conexao = psy.connect(
            user = usuario,
            password = senha,
            host = host,
            dbname = database
        )

    def inserir_na_categoria(self,categoria=Categoria):
        cursor = self.conexao.cursor()
        query = ('INSERT INTO categoria (nome,tipo,descricao) VALUES (%s,%s,%s);')
        valor = (categoria.nome,categoria.tipo,categoria.descricao)
        cursor.execute(query,valor)
        self.conexao.commit()
        return True
    
database = Database('postgres','marcos28','localhost','sistema_financeiro')
teste = Categoria('salário mensal','receita','dadadsadsadsa')
print(database.inserir_na_categoria(teste))