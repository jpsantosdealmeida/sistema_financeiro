import model.database as mdb
from model.transacao import Transacao

class TransacaoController:
    
    @staticmethod
    def inserir(transacao : Transacao):
        conexao = mdb.Database.obter_conexao()
        try:
            curso = conexao.cursor()
            query = 'INSERT INTO transacaocao (tipo,valor,descricao,data_transacaocao,data_registro) VALUES (%s,%s,%s,%s,%s)'
            values = (transacao.categoria.tipo,transacao.valor,transacao.categoria.descricao,transacao.data_transacao,transacao.data_registro)
            curso.execute(query,values)
            conexao.commit()
            mdb.logging.info(f'SUCESSO: Transacao tipo {transacao.categoria.tipo} inserida.')
            return True
            
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar inserir {transacao.categoria.tipo}: {e}.' )
            return e

    @staticmethod  
    def deletar(id_transacao):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = 'DELETE FROM transacao WHERE id=%s'
            value = (id_transacao,)
            cursor.execute(query,value)
            mdb.logging.info(f'SUCESSO: Transacao com id: {id_transacao} deletada.')
            return True
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar deletar transacao de id {id_transacao}: {e}.' )
            return e

    @staticmethod
    def atualizar(transacao: Transacao, id_transacao):
        conexao = mdb.Database.obter_conexao()
        campos = []
        valores = []

        if transacao.categoria.tipo:
            campos.append('tipo=%s')
            valores.append(transacao.categoria.tipo)

        if transacao.valor:
            campos.append('valor=%s')
            valores.append(transacao.valor)

        if transacao.categoria.descricao:
            campos.append('descricao=%s')

        if transacao.data_transacao:
            campos.append('data_transacao=%s')
            valores.append(transacao.data_transacao)

        if transacao.data_registro:
            campos.append('data_registro=%s')
            valores.append(transacao.data_registro)

        try:
            cursor = conexao.cursor()
            query = f'UPDATE transacao SET {" ,".join(campos)} WHERE id=%s'
            valores.append()
            cursor.execute(query,tuple(valores))
            conexao.commit()
            mdb.logging.info(f'SUCESSO: Transação com id: {id_transacao} atualizada.' )
            return True
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar atualizar transação de id: {id_transacao}: {e}.' )
            return e
            


    @staticmethod
    def listar_todos():
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM transacao')
            results = cursor.fetchall()
            mdb.logging.info(f'SUCESSO: Transacões selecionadas.' )

            return results
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar transações : {e}.' )
            return e

    
    @staticmethod
    def lista_um(id_transacao):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = 'SELECT * FROM transacaocao WHERE id=%s'
            value = (id_transacao,)
            cursor.execute(query,value)
            result = cursor.fetchone()
            mdb.logging.info(f'SUCESSO: Transação de id: {id_transacao} selecionada.' )
            return result
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a transação de id: {id_transacao}: {e}.' )
            return e