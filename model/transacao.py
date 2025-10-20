from dataclasses import dataclass
from datetime import date
from .categoria import Categoria
@dataclass
class Transacao:
    categoria: Categoria
    # tipo: str categoria.tipo
    valor: float
    # descricao: str categoria.descricao
    data_transacao: date
    data_registro: date
    
