from src.__math_operations import addition, soustraction, multiplication, division
from src.string_operations import concatener, mettre_en_majuscules

def main():
    # les fonctions mathématiques + * / -
    print("Addition:", addition(4, 5))
    print("Soustraction:", soustraction(10, 7))
    print("Multiplication:", multiplication(3, 3))
    print("Division:", division(10, 2))

    # les fonctions de manipulation de chaînes
    print("Concaténation:", concatener("ilham", " bouaoud"))
    print("Majuscules:", mettre_en_majuscules("taghazout"))

if __name__ == "__main__":
    main()
