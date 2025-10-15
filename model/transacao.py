from dataclasses import dataclass
from datetime import datetime,date

@dataclass
class Transacao:
    id_categoria: int
    tipo: str
    valor: float
    descricao: str
    data_transacao: date
    data_registro: date
