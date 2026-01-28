from model.compte import Compte
from view.vue_solde import VueSolde
from view.vue_operations import VueOperations
from view.vue_alert import VueAlert
from controller.compte_controller import CompteController

if __name__ == "__main__":
    compte = Compte()
    vue_solde = VueSolde()
    vue_ops = VueOperations()
    vue_alert = VueAlert()

    controller = CompteController(compte, vue_solde, vue_ops, vue_alert)

    controller.deposer(100)
    controller.retirer(50)
    controller.retirer(100)