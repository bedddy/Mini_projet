class CompteBancaire:
    def __init__(self):
        self.solde = 0
        self.historique = []

    def depot(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt : +{montant}")

    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            self.historique.append(f"Retrait : -{montant}")
        else:
            self.historique.append("Retrait refusé : solde insuffisant")

    def get_solde(self):
        return self.solde

    def get_historique(self):
        return self.historique



if __name__ == "__main__":
    compte1 = CompteBancaire()
    compte2 = CompteBancaire()

    compte1.depot(100)
    compte2.depot(50)
    compte1.retrait(34)

    print("Compte1 solde:", compte1.get_solde())  # 100
    print("Compte2 solde:", compte2.get_solde())  # 50
    