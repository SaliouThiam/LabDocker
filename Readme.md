## Description de l'application :

Cette application est une **API REST** développée avec **Flask** et utilise **SQLite** comme base de données. Elle permet de :
- **Ajouter** des Etudiant dans la table  **DIC2_GIT** (via une requête POST).
- **Récupérer** tous les Etudiants stockés dans la table **DIC2_GIT** (via une requête GET).

L'application est conteneurisée avec **Docker**  et fichier SQLite est stocké dans un volume pour garantir la persistance des données entre les arrêts et redémarrages du conteneur.

### Détails de la base de données :

Lorsque l'application démarre, elle crée automatiquement une base de données SQLite dans le fichier `/data/database.db`. 

#### Structure de la table **DIC2_GIT** :
La table **`DIC2_GIT`** contient deux colonnes :
- **`id`** : Clé primaire auto-incrémentée.
- **`nom`** : Texte non nul représentant le nom à stocker.

---

## Commandes :

### Récupération depuis Docker Hub :

1. **Puller l'image** depuis Docker Hub :
   ```bash
   docker pull saliou094/projetdocker-api:latest
   ```

2. **Exécuter l'image** avec Docker :
   ```bash
   docker run -d -p 5000:5000 -v $(pwd)/data:/data saliou094/projetdocker-api:latest
   ```

### Exécution avec Docker Compose :

Si  on veux, on peut utiliser Docker Compose avec la commande ci dessous :

1. **Exécuter avec Docker Compose** :
   ```bash
   docker-compose up
   ```

Cela va automatiquement monter le répertoire de données, créer les volumes, et exécuter l'application.

---

## Requêtes API :

### Requête GET :

- Pour **récupérer toutes les entrées** de la table **DIC2_GIT**, accède à l'URL suivante dans un navigateur ou avec cURL :
  ```
  http://localhost:5000/api/items
  ```

### Requête POST :

- Pour **ajouter une nouvelle entrée** dans la table **DIC2_GIT**, utilise une requête POST avec un payload JSON.

#### Sur Postman :

1. Choisir la méthode **POST**.
2. Utiliser l'URL suivante : `http://localhost:5000/api/items`
3. Dans l'onglet **Body**, choisir **raw** et **JSON** et entrer le contenu suivant :
   ```json
   {
       "nom": "Le nom de la personne"
   }
   ```

#### Ligne de commande (en utilisant cURL) :

1. Pour ajouter une entrée avec cURL :
   ```bash
   curl -X POST http://localhost:5000/api/items -H "Content-Type: application/json" -d '{"nom": "Le nom de la personne"}'
   ```

2. Exemple avec un nom spécifique :
   ```bash
   curl -X POST http://localhost:5000/api/items -H "Content-Type: application/json" -d '{"nom": "Serigne Saliou Thiam"}'
   ```

---
