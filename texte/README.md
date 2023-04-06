# ENSAE 1A : projet de programmation


Ce dépôt contient le projet informatique sur l'optimisation d'un réseau de livraison de LAGIER Charles et de Lauze Tony, en 1A ENSAE. 


Ce dépôt contient plusieurs dossiers et fichiers : 
- le dossier `delivery_network` contient le code principal 
    - C'est là qu'est la classe Graph est implémentée, dans le fichier `graph`. 
    - Le ficher `trajey_truk` contient des programmes permetant de trouver des allocations répondant au problème.
    - les fichiers `s2_time_calcul_with_mst` et `séance2_time_calcul` sont des programmes trouvant les puissances minimuns nécessaires à la résolution du problème
    - le fichier `Unionfind` permet l'implémentationde la classe UnionFind 
    - les fichiers `creation_output` et `realistic_solution` permettent de traiter le cas réaliste
    - le fichier `algo_gen` est une implémentation d'un algorithme génétique utiliser pour résoudre le problème
    - le fichier `visual_presentation` permet d'obtenir des résulats graphiques
        
- le dossier `inputs` contient des jeux de données (graphes et ensembles de trajets) 
    - le dossier `truck` contient le catalogue de camion
    - le dossier `network_importation` contient les fichiers de graphes et des routes associées
- le dossier `tests` contient les tests unitaires
- le dossier `texte` contient plusieurs documents texte explicatant certains aspects du programme
- le dossier `result` contient les résulats graphiques
- le fichier `install_graphviz.sh` permet d'installer graphviz sur sspcloud
`