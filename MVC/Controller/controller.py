class CompteController:
    def __init__(self, compte, vue_solde, vue_ops, vue_alert):
        self.compte = compte
        self.vue_solde = vue_solde
        self.vue_ops = vue_ops
        self.vue_alert = vue_alert

    def deposer(self, montant):
        self.compte.deposer(montant)
        self.mettre_a_jour_vues()

    def retirer(self, montant):
        # Vérification du solde avant de retirer
        if montant > self.compte.get_solde():   # <-- corrigé ici
            print("Retrait refusé : solde insuffisant")
            return

        # Effectuer le retrait seulement si le solde est suffisant
        self.compte.retirer(montant)
        self.mettre_a_jour_vues()

    def mettre_a_jour_vues(self):
        self.vue_solde.afficher(self.compte.get_solde())
        self.vue_ops.afficher(self.compte.get_historique())
        self.vue_alert.verifier(self.compte.get_solde())
