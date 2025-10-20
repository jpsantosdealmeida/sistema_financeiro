from model.categoria import Categoria
from controller.categoria_controller import CategoriaController
from model.transacao import Transacao
from controller.trasacao_controller import TransacaoController

categoria_lazer = Categoria('lazer','receita','restaurantes')
t1 = Transacao(categoria_lazer,1000,'2025-10-10','2025-10-10')
a = (CategoriaController.listar_todos())


TransacaoController.inserir(t1)
