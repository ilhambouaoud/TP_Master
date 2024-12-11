def analyse_texte(text):
    
    nbreCaracteres = len(text)
    nbreMots = len(texte.split())
    
    return {
        'nbreMots': nbreMots,
        'nbreCaracteres': nbreCaracteres
    }


texte = "Bonjour tout le monde !"
rslt = analyse_texte(texte)
print(rslt) 