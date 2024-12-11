def intersection(ensemble1,ensemble2):
    return ensemble1.intersection(ensemble2)

ensemble1 = {1, 2, 3, 4}
ensemble2 = {3, 4, 5, 6}

inter = intersection(ensemble1, ensemble2)
print("L'intersection des deux ensembles ' :")
print(inter)