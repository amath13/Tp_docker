 ### Rapport de Test Fonctionnel du Site Vie-Publique.sn
**Description**
Ce rapport présente les tests fonctionnels et automatisés réalisés sur le site Vie-Publique.sn. Le but est de vérifier que le site exécute les fonctions attendues en matière de navigation, sécurité, filtrage, et gestion des articles. Une attention particulière est portée à l'automatisation des tests avec Selenium et Pytest, accompagnée d'un rapport de Coverage pour évaluer la qualité des tests.
### Système d'exploitation utilisé OS : Windows 10
                  
**Tests Fonctionnels**

**Cas de Test 1** : Accès à la page des actualités
•	Objectif : Vérifier que l'utilisateur peut accéder à la page des actualités.
•	Étapes :
1.	Ouvrir un navigateur.
2.	Saisir l'URL https://www.vie-publique.sn/publications/actualites  dans la barre d'adresse.
3.	Appuyer sur Entrée.
•	Résultat attendu : La page des actualités se charge avec succès et affiche une liste d'articles.
•	Résultat réel : Succès : La page des actualités se charge correctement et affiche une liste d'articles.


**Cas de Test 2**: Affichage du détail d'une actualité
•	Objectif : Vérifier que l'utilisateur peut afficher le détail d'une actualité.
•	Étapes :
1.	Accéder à la page des actualités.
2.	Cliquer sur un titre d'article.
•	Résultat attendu : La page de détail de l'article sélectionné s'affiche avec le contenu complet.
•	Résultat réel : Succès : L'utilisateur peut voir en détail l'article sélectionné


**Cas de Test 3** : Recherche d'actualités
•	Objectif : Vérifier que l'utilisateur peut rechercher des articles d'actualité en utilisant un mot-clé.
•	Étapes :
1.	Accéder à la page des actualités.
2.	Saisir un mot-clé pertinent dans la barre de recherche (exemple : "économie").
3.	Cliquer sur le bouton de recherche ou appuyer sur Entrée.
•	Résultat attendu : Une liste d'articles correspondants au mot-clé s'affiche.
•	Résultat réel : Échec : Il n'y a pas de champ de recherche sur la page pour entrer un mot-clé.


**Cas de Test 4** : Filtrage des actualités par catégorie
•	Objectif : Vérifier que l'utilisateur peut filtrer les actualités par catégorie.
•	Étapes :
1.	Accéder à la page des actualités.
2.	Sélectionner une catégorie dans la liste déroulante ou dans le menu des filtres (ex. : "Communiqué").
•	Résultat attendu : Seules les actualités appartenant à la catégorie sélectionnée s'affichent.

•	Résultat réel : Filtrage en place, les actualités sont correctement filtrées en fonction de la catégorie sélectionnée. Les options de filtrage sont visibles et fonctionnelles.


**Cas de Test 5** : Ouverture d'un article dans un nouvel onglet
•	Objectif : Vérifier que l'utilisateur peut ouvrir un article d'actualités dans un nouvel onglet.
Étapes :
1.	Accéder à la page des actualités.
2.	Cliquer avec le bouton droit sur un article.
3.	Sélectionner l'option "Ouvrir le lien dans un nouvel onglet".
4.	Vérifier que l'article s'ouvre correctement dans un nouvel onglet.
.
•	Résultat attendu : L’article sélectionné s'ouvre correctement dans un nouvel onglet, permettant à l'utilisateur de consulter plusieurs articles sans quitter la page d'actualités principale.

•	Résultat réel :  L'article s'ouvre correctement dans un nouvel onglet.


**Cas de Test 6** : Test du lien de retour à l'accueil
•	Objectif : Vérifier que l'utilisateur peut revenir à la page d'accueil depuis la page des "Conseil des ministres"
Étapes :
1.	Accéder à la page d'accueil du site.
2.	Naviguer vers la section Conseil des ministres à partir du menu de navigation.
3.	Cliquer sur la flèche de retour du navigateur pour vérifier si l'utilisateur revient à la page d'accueil.
•	Résultat attendu : L'utilisateur est redirigé vers la page d'accueil après avoir utilisé la flèche de retour du navigateur.

•	Résultat réel : La flèche de retour ramène correctement l'utilisateur vers la page d'accueil.


**Cas de Test 7** : Vérification du SSL
•	Objectif : Vérifier que le site utilise une connexion sécurisée via SSL.
Étapes :
1.	Ouvrir un navigateur.
2.	Saisir l'URL https://www.vie-publique.sn/publications/actualites dans la barre d'adresse.
3.	Vérifier si le cadenas de sécurité s'affiche à côté de l'URL.
•	Résultat attendu : Le site est sécurisé, avec une URL commençant par https et un cadenas visible à côté de l'URL.

•	Résultat réel : Le site est sécurisé, le cadenas de sécurité est visible et l'URL commence par https.


### Recommandations

1. Ajouter une fonctionnalité "Abonnez-vous à nos lettres d’information"
Objectif : Permettre aux utilisateurs de s'abonner facilement aux newsletters.
Détail :
Ajouter une option visible pour permettre l'abonnement à une newsletter.
Un bouton "Abonnez-vous" pourrait rediriger vers un formulaire d'inscription.
2. Mettre en place une barre de recherche
Objectif : Améliorer l'expérience utilisateur en facilitant la recherche de contenu.
Emplacement recommandé : En haut à droite ou dans le menu de navigation.


### Tests Automatisés avec Selenium

J'ai réalisé une série de tests automatisés pour vérifier les fonctionnalités du site [vie-publique.sn](https://www.vie-publique.sn/) à l'aide de **Selenium** et **Pytest**. Les tests ont été effectués dans un environnement Python.

Les tests couvrent plusieurs aspects, notamment :

- L'accès à différentes sections du site
- La navigation entre les pages
- Les interactions avec les éléments de l'interface utilisateur
- La gestion des overlays et des fenêtres contextuelles

### Outils Utilisés

- **Langage** : Python
- **Framework de test** : Pytest
- **Outil d'automatisation de navigateur** : Selenium WebDriver
- **Rapport de couverture** : Pytest-Cov

### Couverture de Code

NB : J'ai utilisé **pytest-cov** pour générer un rapport de couverture de code. Pour le moment, la couverture de test est de **80%**, et je m'engage à développer régulièrement de nouveaux tests pour augmenter cette couverture.

### Instructions pour Exécuter les Tests

1. Créer et activer un environnement virtuel sous Windows avec PowerShell :

    ```powershell
    myvenv\Scripts\activate
    ```

2. Exécuter les tests et générer un rapport de couverture :

    ```powershell
    pytest --cov=. --cov-report=html
    ```

3. Visualiser le rapport de couverture :

    ```powershell
    start htmlcov/index.html
    ```

### Prochaines Étapes

- Augmenter la couverture de code en développant davantage de tests pour couvrir tous les cas d'usage importants.
- Améliorer la robustesse des tests pour les différents scénarios.
