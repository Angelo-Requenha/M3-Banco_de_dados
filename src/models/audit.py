from datetime import datetime

class Audit:
    def __init__(self, tipo: str, referencia_id: int, acao: str, data_evento: datetime):
        self.tipo: str = tipo
        self.referencia_id: int = referencia_id
        self.acao: str = acao
        self.data_evento: datetime = data_evento

    def get_tipo(self) -> str:
        return self.tipo

    def get_referencia_id(self) -> int:
        return self.referencia_id

    def get_acao(self) -> str:
        return self.acao

    def get_data_evento(self) -> datetime:
        return self.data_evento
