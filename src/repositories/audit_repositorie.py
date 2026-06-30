from config.database import connect_db
from src.models.audit import Audit

class AuditRepository:
    def __init__(self):
        self.connection = connect_db()

    def get_all_audit(self) -> list[Audit]:
        cursor = self.connection.cursor()
        query = "SELECT tipo, referencia_id, acao, data_evento FROM vw_auditoria ORDER BY data_evento DESC"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return [Audit(tipo=row[0], referencia_id=row[1], acao=row[2], data_evento=row[3]) for row in results]

    def get_audit_report(self) -> list[dict]:
        cursor = self.connection.cursor()
        query = "SELECT tipo, acao, COUNT(*) AS total FROM vw_auditoria GROUP BY tipo, acao ORDER BY tipo, acao"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return [{"tipo": row[0], "acao": row[1], "total": row[2]} for row in results]
