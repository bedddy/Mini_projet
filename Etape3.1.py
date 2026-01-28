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
