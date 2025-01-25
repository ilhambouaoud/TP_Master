class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age < 0:
        raise NegativeAgeError("l'age ne doit pas etre negatif ")
    print(f"age = {age} ans.")
try:
    set_age(-6)  
except NegativeAgeError as e:
    print("Erreur :", e)
