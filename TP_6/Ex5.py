def process_input(user_input):
    try:
       val = int(user_input)
       res = 10 /val
       print(f"10/{val} = {res}")
    except ValueError:
       print(f"Erreur : {user_input} doit etre un entier")
    except ZeroDivisionError:
       print("Erreur : Division par zéro interdit")
input = "0"
process_input(input)