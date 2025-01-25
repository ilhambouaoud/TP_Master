def safe_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro est interdit!!!!")
    else:
        print("La division a été effectuée avec succès")
        print("Résultat :", res)
    finally:
        print("La fonction est terminée")
safe_division(10, 2)