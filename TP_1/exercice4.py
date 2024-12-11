def compte_occurrences(liste):
    return {mot: liste.count(mot) for mot in set(liste)}

mots = ["mathematiques", "physiques", "svt", "physiques", "arabe", "svt", "svt"]
result= compte_occurrences(mots)
print("Les occurenses de chaque mot :", result)