# Ce document contient les réponses aux questions portant sur la complexité des algorithmes.

On note : 
V le nombre de sommets dans le graphe
E le nombre d'arrêtes dans le graphe


# Séance 1

Question 3 : 
Dans le pire des cas, l'algorithme parcourt l'ensemble des noeuds du graphe. La complexité est donc polynomiale : O(V). 

Question 5 :

On utilise l'algorythme de Djikistra. On parcourt tout les noeuds et toutes les arrêtes. Il y a un test binaire pour déterminer si le noeud doit être ajouté au chemin.
La complexité est donc polynomiale et vaut O((E+V)log(E)).

Question 6 :

On réalise une recherche binaire de complexité logarithmique. A chaque itération, on utilise l'algorithme de Dijkstra. 
On note P la puissance maximun trouvée dans le graphe. 
La complexité est donc polynomiale et vaut O(log(P)*(E+V)log(E)).


# Séance 2

Question 6 : 

Les fonctions find() et union() ont pour complexité O(E).
On parcourt ensuite l'ensemble des arrêtes.

La complexité est donc polynomiale et vaut O(E*log(E))

Question 9 :

On utilise un algorithme de parcours en profondeur qui examine, dans le pire des cas, l'ensemble des noeuds de l'arbre couvrant.
La complexité est donc polynomiale et est O(V)