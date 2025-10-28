import model.database as mdb
from model.transacao import Transacao


class TransacaoController:
    
    @staticmethod
    def inserir(transacao : Transacao):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = 'INSERT INTO transacao (tipo,valor,descricao,data_transacao,data_registro) VALUES (%s,%s,%s,%s,%s)'
            values = (transacao.categoria.tipo,transacao.valor,transacao.categoria.descricao,transacao.data_transacao,transacao.data_registro)
            cursor.execute(query,values)
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
            valores.append(id_transacao)
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
    def listar_um(id_transacao):
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            query = 'SELECT * FROM transacao WHERE id=%s'
            value = (id_transacao,)
            cursor.execute(query,value)
            result = cursor.fetchone()
            mdb.logging.info(f'SUCESSO: Transação de id: {id_transacao} selecionada.' )
            return result
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a transação de id: {id_transacao}: {e}.' )
            return e
        

    @staticmethod  
    def view_treeview():
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM visualizacao_frame_main')
            linhas_view = cursor.fetchall()
            mdb.logging.info(f'SUCESSO: View visualizacao_frame_main selecionada.' )
            return linhas_view
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a view visualizacao_frame_main: {e}.' )
            return e
        
    @staticmethod
    def view_treeview_filtrada(dt_inicio=None,dt_final=None,categoria=None,tipo=None):
        conexao = mdb.Database.obter_conexao()
        condicoes = []
        valores = []

        # Filtro das datas
        if dt_inicio and dt_final:
            condicoes.append('data BETWEEN %s AND %s')
            valores.extend([dt_inicio, dt_final])
        elif dt_inicio:
            condicoes.append('data >= %s')
            valores.append(dt_inicio)
        elif dt_final:
            condicoes.append('data <= %s')
            valores.append(dt_final)

        if categoria:
            condicoes.append('categoria = %s')
            valores.append(categoria)

        if tipo:
            condicoes.append('tipo = %s')
            valores.append(tipo)



        try:
            cursor = conexao.cursor()
            query = 'SELECT * FROM visualizacao_frame_main '
            if condicoes:
                query += ' WHERE ' + ' AND ' .join(condicoes)
                values = tuple(valores)
                cursor.execute(query,values)
                linhas_view_filtradas = cursor.fetchall()
                return linhas_view_filtradas
        except mdb.Error as e:
            return e
            


    @staticmethod    
    def view_treeview_transacoes():
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM transacoes_frame_transacoes')
            linhas_view = cursor.fetchall()
            mdb.logging.info(f'SUCESSO: View transacoes_frame_transacoes selecionada.' )
            return linhas_view
        
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a view transacoes_frame_transacoes: {e}.' )
            return e
        
    @staticmethod
    def view_treeview_transacoes_filtrada(dt_inicio=None,dt_final=None,categoria=None,tipo=None):
        conexao = mdb.Database.obter_conexao()
        condicoes = []
        valores = []

        # Filtro das datas
        if dt_inicio and dt_final:
            condicoes.append('data BETWEEN %s AND %s')
            valores.extend([dt_inicio, dt_final])
        elif dt_inicio:
            condicoes.append('data >= %s')
            valores.append(dt_inicio)
        elif dt_final:
            condicoes.append('data <= %s')
            valores.append(dt_final)

        if categoria:
            condicoes.append('categoria = %s')
            valores.append(categoria)

        if tipo:
            condicoes.append('tipo = %s')
            valores.append(tipo)



        try:
            cursor = conexao.cursor()
            query = 'SELECT * FROM transacoes_frame_transacoes '
            if condicoes:
                query += ' WHERE ' + ' AND ' .join(condicoes)
                values = tuple(valores)
                cursor.execute(query,values)
                linhas_view_filtradas = cursor.fetchall()
                return linhas_view_filtradas
        except mdb.Error as e:
            return e
            













 
    @staticmethod
    def filtro_categoria_transacoes():
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT DISTINCT(categoria) FROM transacoes_frame_transacoes')   
            linha_categorias = list(cursor.fetchall())
            lista_categorias = []
            for categoria in linha_categorias:
              lista_categorias.append(categoria[0])
            return lista_categorias
            
            # return linhas_categorias
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a view transacoes_frame_transacoes: {e}.' )
            return e
        
    @staticmethod
    def filtro_tipo_transacoes():
        conexao = mdb.Database.obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT DISTINCT(tipo) FROM transacoes')   
            linhas_tipo = list(cursor.fetchall())
            lista_tipos = []
            for tipo in linhas_tipo:
              lista_tipos.append(tipo[0])
            return lista_tipos
            
            # return linhas_categorias
        except mdb.Error as e:
            mdb.logging.error(f'ERRO ao tentar selecionar a view transacoes_frame_transacoes: {e}.' )
            return e
        


