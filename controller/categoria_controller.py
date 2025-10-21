import model.database as mdb
from model.categoria import Categoria

class CategoriaController:

    @staticmethod
    def inserir(categoria : Categoria):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = ('INSERT INTO categoria (nome,tipo,descricao) VALUES (%s,%s,%s)')
            values = (categoria.nome,categoria.tipo,categoria.descricao)
            cursor.execute(query,values)
            conexao.commit()
            mdb.logging.info(f'SUCESSO: categoria {categoria.nome} inserida.' )
            return True
        
        except mdb.mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar inserir {categoria.nome}: {e}.' )

    @staticmethod
    def deletar(id_categoria):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = ('DELETE FROM categoria WHERE id = (%s)')
            value = (id_categoria,)
            cursor.execute(query,value)
            conexao.commit()
            mdb.logging.info(f'SUCESSO: categoria com id: {id_categoria} deletada.' )
            
            return True
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar deletar categoria de id: {id_categoria}: {e}.' )


    @staticmethod
    def atualizar(categoria : Categoria,id_categoria):
        conexao = mdb.Database.obter_conexao()
        campos = []
        valores = []

        if categoria.nome:
            campos.append('nome=%s')
            valores.append(categoria.nome)

        if  categoria.tipo:
            campos.append('tipo=%s')
            valores.append(categoria.tipo)

        if categoria.descricao:          
            campos.append('descricao=%s')
            valores.append(categoria.descricao)

        try:
            cursor = conexao.cursor()
            query = f'UPDATE categoria SET {" ,".join(campos)} WHERE id = %s'
            valores.append(id_categoria)
            cursor.execute(query,tuple(valores))
            conexao.commit()
            mdb.logging.info(f'SUCESSO: categoria com id: {id_categoria} atualizada.' )
            return True

        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar atualizar categoria de id: {id_categoria}: {e}.' )

    @staticmethod
    def listar_todos():
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM categoria')
            results = cursor.fetchall()
            mdb.logging.info(f'SUCESSO: Categorias selecionadas.' )

            return results
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar categorias : {e}.' )

    
    @staticmethod
    def lista_um(id_categoria):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = 'SELECT * FROM categoria WHERE id=%s'
            value = (id_categoria,)
            cursor.execute(query,value)
            result = cursor.fetchone()
            mdb.logging.info(f'SUCESSO: Categoria de id: {id_categoria} selecionada.' )
            return result
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a categoria de id: {id_categoria}: {e}.' )

