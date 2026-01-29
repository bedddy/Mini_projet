from Model.model import Compte
from View.vue_solde import VueSolde
from View.vue_op import VueOperations
from View.vue_alrt import VueAlert
from Controller.controller import CompteController


if __name__ == "__main__":
    # -------------------
    # 1️⃣ Création du modèle
    # -------------------
    compte = Compte()

    # -------------------
    # 2️⃣ Création des vues
    # -------------------
    vue_solde = VueSolde()
    vue_ops = VueOperations()
    vue_alert = VueAlert()

    # -------------------
    # 3️⃣ Création du contrôleur
    # -------------------
    controller = CompteController(compte, vue_solde, vue_ops, vue_alert)

    # -------------------
    # 4️⃣ Test des opérations MVC
    # -------------------

    print("\n=== Dépôt de 100 ===")
    controller.deposer(100)      # Solde = 100, historique ["Dépôt +100"]

    print("\n=== Retrait de 50 ===")
    controller.retirer(50)       # Solde = 50, historique ["Dépôt +100", "Retrait -50"]

    print("\n=== Retrait de 100 (solde négatif) ===")
    controller.retirer(100)      # Solde = -50, alerte déclenchée

    print("\n=== Dépôt de 200 ===")
    controller.deposer(200)      # Solde = 150, alerte disparue
