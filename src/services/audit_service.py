from src.repositories.audit_repositorie import AuditRepository

class AuditService:
    def __init__(self):
        self.audit_repository = AuditRepository()

    def get_all_audit(self):
        return self.audit_repository.get_all_audit()

    def get_audit_report(self):
        return self.audit_repository.get_audit_report()
