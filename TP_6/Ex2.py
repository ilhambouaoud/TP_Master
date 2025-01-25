def convert_to_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        raise ValueError(f"La conversion de {val} en entier a échoué!!!!")
try:
    result = convert_to_int("abc") 
    print("Résultat :", result)
except ValueError as e:
    print("Erreur :", e)
