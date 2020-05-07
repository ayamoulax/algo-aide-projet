### consigne: faire un algo qui classe les personnes dans une liste de celui qui t'a le plus aidé à celui qui t'a le moins aidé ###


# on crée une liste qui contient le prénom de tous les élèves
TodosLosAlumnos = ['Aya', 'Fatima', 'Dayna', 'Nour', 'Aminata', 'Yannis', 'Rémi', 'Walid', 'Younes', 'Sidy', 'Kevin', 'Yassine', 'Alexendre', 'Adem', 'Othman', 'Nouredine', 'Ruben', 'Nolan', 'Clément', 'Jeras', 'Soussi', 'Mehdi']

# on fait une fonction qui va ajouter les 3 personnes qu ont le plus aidé l'utilisateur dans une liste vide
def func(a):
    #création de liste vide
    ListeVide = []
    #on fait un input pour connaitre les personnes qui ont aidé
    a = input ('Quelles sont les 3 personnes qui vous ont le plus aidé ? :  ')
    #on convertit les string en éléments de liste
    a = print(a.split())

#si le prénom de la personne est le premier élément de la liste, on affiche l'élément suivi du nombre de points qu'il lui est attribué.

    if a.index()== 0 :
        print (a.index)
        print ('20 points')

# si le prénom de la personne est le deuxième élément de la liste, on affiche l'élément suivi du nombre de points qu'il lui est attribué.


    if a.index()== 1 :
        print (a.index)
        print ('15 points')

# si le prénom de la personne est le premier élément de la liste, on affiche l'élément suivi du nombre de points qu'il lui est attribué.


    if a.index()== 2:
        print (a.index)
        print ('10 points')

# on ajoute cela à la liste vide.
    ListeVide.append(a)

# puis, on renvoie la liste.
    return ListeVide






