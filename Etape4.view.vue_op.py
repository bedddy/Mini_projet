class VueOperations:
    def afficher(self, historique):
        print("[OPERATIONS]")
        for op in historique:
            print(f" - {op}")