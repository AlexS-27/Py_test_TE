from operator import truediv


def ajouter_article(name, price, quantity):
     """
     Fonction qui simule l'ajout d'un article dans le panier
     :param name: chaîne de caractère
     :param price: float
     :param quantity: integer

     Lève ValueError ou TypeError selon les cas et ajoute si le même article et recommandé
     Retourne un ajout dans le dictionnaire du produit ou additionne pour la quantité
     """

     panier = {"pomme": 2}

     #vérification basiques
     if not isinstance(name, str):
         raise TypeError("Le nom doit être une chaîne de caractère")
     if not isinstance(price, float):
         raise ValueError("Le prix ne doit contenir aucun autre caractère que des chiffres à virgule")
     if not isinstance(quantity, int):
         raise ValueError("La quantité ne doit être que des chiffres sans virgules")
     if quantity <= 0:
         raise ValueError("Quantité inférieur ou égale à zéro")
     if price <= 0:
         raise ValueError("Prix inférieur ou égale à zéro")
     if panier.keys() == name:
         return "Quantité ajoutée"
     return True

