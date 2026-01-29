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
    
def main():
    # Création de deux "comptes"
        compte1 = CompteBancaireSingleton()
        compte2 = CompteBancaireSingleton()

        # Dépôts et retraits
        compte1.depot(1000)
        compte2.retrait(300)
        compte1.depot(500)
        compte2.retrait(1200)  # retrait refusé

        # Affichage du solde
        print("Solde compte 1 :", compte1.get_solde())
        print("Solde compte 2 :", compte2.get_solde())

        # Vérifier que c'est bien la même instance
        print("Meme instance ?", compte1 is compte2)

        # Historique des opérations
        print("\nHistorique des opérations :")
        for op in compte1.historique:
            print("-", op)


# Point d'entrée du programme
if __name__ == "__main__":
        main()
