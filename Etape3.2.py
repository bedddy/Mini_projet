class VueSolde:
    def update(self, compte):
        print(f"[SOLDE] Nouveau solde : {compte.solde} dt")

class VueOperations:
    def update(self, compte):
        print("[OPERATIONS] Historique des opérations:")
        for op in compte.historique:
            print(f" - {op}")

class VueAlert:
    def update(self, compte):
        if compte.solde < 0:
            print("⚠️ ALERTE : solde négatif !")