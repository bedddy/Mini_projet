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
    
        compte1 = CompteBancaireSingleton()
        compte2 = CompteBancaireSingleton()

        
        compte1.depot(1000)
        compte2.retrait(300)
        compte1.depot(500)
        compte2.retrait(1200)  

        
        print("Solde compte 1 :", compte1.get_solde())
        print("Solde compte 2 :", compte2.get_solde())

       
        print("Meme instance ?", compte1 is compte2)

        
        print("\nHistorique des opérations :")
        for op in compte1.historique:
            print("-", op)



if __name__ == "__main__":
        main()
