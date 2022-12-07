# Advent of Code 2022
### Day 1
La jungle doit être trop envahie et difficile à parcourir en véhicule ou à atteindre depuis les airs
l'expédition des Elfes se fait traditionnellement à pied.
Lorsque vos bateaux approchent de la terre, les Elfes commencent à faire l'inventaire de leurs provisions.
La nourriture est un élément important à prendre en compte, en particulier le nombre de calories que chaque Elfe transporte

À tour de rôle, les lutins notent le nombre de calories contenues dans les différents repas, en-cas, rations, etc.
qu'ils ont apportés avec eux, un article par ligne.
Chaque lutin sépare son propre inventaire de celui du lutin précédent (s'il y en a un) par une ligne blanche.

Par exemple, supposons que les Elfes finissent d'écrire les Calories de leurs articles et se retrouvent avec la liste suivante :
```
[
1000
2000
3000

4000

5000
6000

7000 
8000 
9000

10000
]
```


Cette liste représente les Calories de la nourriture transportée par cinq Elfes :

    Le premier Elfe transporte des aliments contenant 1000, 2000 et 3000 Calories, soit un total de 6000 Calories.
    Le deuxième Elfe transporte un aliment contenant 4000 Calories.
    Le troisième lutin transporte de la nourriture contenant 5000 et 6000 calories, soit un total de 11000 calories.
    Le quatrième lutin transporte des aliments contenant 7000, 8000 et 9000 Calories, soit un total de 24000 Calories.
    Le cinquième lutin transporte un aliment contenant 10000 calories.

Au cas où les lutins auraient faim et auraient besoin d'un en-cas supplémentaire,
 ils doivent savoir à quel lutin s'adresser : ils aimeraient savoir combien de Calories est transporté par
 le lutin qui porte le plus de Calories. Dans l'exemple ci-dessus, il s'agit de 24000 (portées par le quatrième Elfe).

Trouvez le lutin qui transporte le plus de calories. Combien de calories totales ce lutin transporte-t-il ?

### Answer
L'Elfe avec le plus de calorie est Elf-266 avec un total de 69281
