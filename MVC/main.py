from Model.model import Compte
from View.vue_solde import VueSolde
from View.vue_op import VueOperations
from View.vue_alrt import VueAlert
from Controller.controller import CompteController

if __name__ == "__main__":

   
    compte = Compte()
    vue_solde = VueSolde()
    vue_ops = VueOperations()
    vue_alert = VueAlert()
    controller = CompteController(compte, vue_solde, vue_ops, vue_alert)

    print(" Bienvenue dans l'application bancaire\n")

    while True:
       
        print("\nChoisissez une action :")
        print("1 - Dépôt")
        print("2 - Retrait")
        print("3 - Quitter")

        choix = input("Votre choix (1/2/3) : ").strip()

        if choix == "1":
            montant = input("Montant à déposer : ").strip()
            if montant.isdigit():
                controller.deposer(int(montant))
            else:
                print("Veuillez entrer un nombre valide.")
        elif choix == "2":
            montant = input("Montant à retirer : ").strip()
            if montant.isdigit():
                controller.retirer(int(montant))
            else:
                print("Veuillez entrer un nombre valide.")
        elif choix == "3":
            print("Merci d'avoir utilisé l'application. Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
