class Compte:
    def __init__(self):
        self.solde = 0
        self.historique = []

    def deposer(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt +{montant}")

    def retirer(self, montant):
        self.solde -= montant
        self.historique.append(f"Retrait -{montant}")

    def get_solde(self):
        return self.solde

    def get_historique(self):
        return self.historique
    
