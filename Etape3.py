class Observable:
    def __init__(self):
        self.observateurs = []

    def ajouter_observateur(self, obs):
        if obs not in self.observateurs:
            self.observateurs.append(obs)

    def notifier(self):
        for obs in self.observateurs:
            obs.update(self)


class CompteBancaire(Observable):
    def __init__(self):
        super().__init__()
        self.solde = 0
        self.historique = []

    def depot(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt +{montant}")
        self.notifier()

    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            self.historique.append(f"Retrait -{montant}")
        else:
            self.historique.append("Retrait refusé")
        self.notifier()

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
            print("ALERTE : solde négatif !")
            

def main():
    # Création du compte
    compte = CompteBancaire()

    # Création des observateurs
    vue_solde = VueSolde()
    vue_operations = VueOperations()
    vue_alert = VueAlert()

    # Abonnement des observateurs
    compte.ajouter_observateur(vue_solde)
    compte.ajouter_observateur(vue_operations)
    compte.ajouter_observateur(vue_alert)

    # Dépôt normal
    compte.depot(100)
    print()

    # Forcer un solde négatif (besoin du test)
    compte.solde -= 150
    compte.historique.append("Retrait -150")

    # Notification manuelle
    compte.notifier()


if __name__ == "__main__":
    main()
