# Un Elfe a la tâche importante de charger tous les sacs à dos de fournitures pour le voyage dans la jungle. 
# Malheureusement, cet Elfe n'a pas tout à fait suivi les instructions d'emballage, et quelques articles doivent donc être réorganisés.

# Chaque sac à dos possède deux grands compartiments. 
# Tous les objets d'un type donné sont censés aller dans un seul de ces deux compartiments. 
# L'elfe qui a fait l'emballage n'a pas respecté la règle d'un seul type d'objet par sac à dos.

# Les Elfes ont dressé une liste de tous les objets qui se trouvent actuellement dans chaque sac à dos (votre entrée dans l'énigme), 
# mais ils ont besoin de votre aide pour trouver les erreurs. 
# Chaque type d'objet est identifié par une seule lettre minuscule ou majuscule (autrement dit, a et A désignent des types d'objets différents).

# La liste des articles de chaque sac à dos est donnée sous forme de caractères sur une seule ligne. 
# Un sac à dos donné contient toujours le même nombre d'articles dans chacun de ses deux compartiments,
#  de sorte que la première moitié des caractères représente les articles du premier compartiment,
#  tandis que la seconde moitié des caractères représente les articles du second compartiment.

# Par exemple, supposons que vous ayez la liste suivante du contenu de six sacs à dos :

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

# Le premier sac à dos contient les articles vJrwpWtwJgWrhcsFMMfFFhFp, ce qui signifie que son premier compartiment contient les articles vJrwpWtwJgWr,
#  tandis que le second compartiment contient les articles hcsFMMfFFhFp. Le seul type d'article qui apparaît dans les deux compartiments est le p minuscule.

# Les compartiments du deuxième sac à dos contiennent les articles jqHRNqRjqzjGDLGL et rsFMfFZSrLrFZsSL.
#  Le seul type d'article qui apparaît dans les deux compartiments est le L majuscule.

# Les compartiments du troisième sac à dos contiennent PmmdzqPrV et vPwwTWBwg ; le seul type d'article commun est le P majuscule.

# Les compartiments du quatrième sac à dos ne partagent que le type d'article v.

# Les compartiments du cinquième sac à dos ne partagent que le type d'article t.

# Les compartiments du sixième sac à dos ne partagent que le type d'article s.

# Pour faciliter le réarrangement des articles, chaque type d'article peut être converti en une priorité :

# Les types d'articles minuscules de a à z ont des priorités de 1 à 26.
# Les types d'articles en majuscules de A à Z ont des priorités de 27 à 52.
# Dans l'exemple ci-dessus, la priorité du type d'article qui apparaît dans les deux compartiments de chaque sac à dos est 16 (p), 38 (L), 42 (P), 22 (v), 20 (t) et 19 (s) ;
#  la somme de ces priorités est 157.

# Trouvez le type d'objet qui apparaît dans les deux compartiments de chaque sac à dos. Quelle est la somme des priorités de ces types d'objets ?

import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

with open(ROOT_DIR + '/inputs/day_3.txt') as file:
    bags = file.read().splitlines()

    values = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    points = {}
    
    for value, letter in enumerate(values, 1):
        points[letter] = value 
    print(points)
    # # for bag in bags:
    #     bag_size = len(bag)
    #     container_size = len(bag) // 2
    #     container_1 = bag[0:container_size]
    #     container_2 = bag[container_size:bag_size]


