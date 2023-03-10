Ce document contient les réponses aux questions portant sur le complexité des algorythmes

On note : 
V le nombre de sommets dans le graphe
E le nombre d'arrêtes dans le graphe

# Séance 1


Question 3 : 
On parcourt dans le pire des cas l'ensemble des noeuds du graphe. La complecité est donc polynomiale O(V). 

Question 5 :

On utilise l'algorythme de Djikistra. On parcourt tout les noeuds et toutes les arrêtes. Il ya a un tets binaire pour déterminer si le noued doit être ajouté au chemin.
La complexité est donc polynomiale et vaut O((E+V)log(E))

Question 6 :

On réalise une recherche binaire de complexité logarithmique.  A chaque itération, on utilise l'algorythme de Djikistra. 
On P la puissance maximun trouvée dans le graphe. 
La complexité est donc polynomiale et vaut O(log(P)*(E+V)log(E))

# Séance 2

Question 6 : 

Les fonctions find a pour complexité O(V)
On parcourt ensuite l'ensemble des arrêtes.
La complexité est donc polynomiale et vaut O(V*E)


Question 9
On utilise un algorithme de parcours en profondeur, qui parcourt au pire l'ensemble des noeuds de l'arbre couvrant.



