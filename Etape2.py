class CompteBancaireSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.solde = 0
            cls._instance.historique = []
        return cls._instance

    def depot(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt : +{montant}")

    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            self.historique.append(f"Retrait : -{montant}")
        else:
            self.historique.append("Retrait refusé")

    def get_solde(self):
        return self.solde