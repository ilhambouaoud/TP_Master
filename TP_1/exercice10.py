def fusionner_dicts(dict1, dict2):
  
    dict1fusion = dict1.copy()
    for cle, valeur in dict2.items():
        if cle in dict1fusion :
            dict1fusion [cle] += valeur
        else:
            dict1fusion [cle] = valeur
    return dict1fusion 


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

fusion = fusionner_dicts(dict1, dict2)
print(fusion)  
