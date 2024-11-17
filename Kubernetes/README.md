# Projet Flask Kubernetes

Ce projet consiste en une application Flask et une base de données SQLite déployées dans un cluster Kubernetes. Ce document explique comment déployer, configurer et tester l'application.





## Étapes de Déploiement

### 1. Construire l'image Docker de l'application Flask


```bash
docker build -t projetdocker-api:latest .
```

### 2. Démarrer Minikube

Lancez un cluster Minikube avec plusieurs nœuds :

```bash
minikube start --nodes=3 --driver=docker
```

### 3. Déployer l'application dans Kubernetes

Appliquez les fichiers de configuration Kubernetes dans l'ordre suivant :

```bash
kubectl apply -f k8s/database-deployment.yaml
kubectl apply -f k8s/database-service.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/backend-networkpolicy.yaml
```

Ces commandes :
- Créent et configurent la base de données SQLite
- Déploient l'application Flask
- Configurent les politiques réseau pour limiter les accès

### 4. Vérifier les déploiements et services

Pour vérifier que les déploiements et services sont bien actifs :

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get networkpolicies
```

### 5. Obtenir l'IP de Minikube et le NodePort pour tester l'API

- Obtenez l'IP de Minikube :

  ```bash
  minikube ip
  ```

- Obtenez le port du `NodePort` :

  ```bash
  kubectl get svc backend-service
  ```

Nous avons choisi le port 30001

## Tester l'API

Vous pouvez utiliser `curl` ou un outil comme Postman pour tester les endpoints de l'application Flask.

### Exemple de Tests avec `curl`

1. **Ajouter un item dans la base de données** :
   ```bash
   curl -X POST http://<minikube-ip>:<node-port>/api/items -H "Content-Type: application/json" -d '{"Saliou": "Thiam"}'
   ```

2. **Récupérer les items** :
   ```bash
   curl http://<minikube-ip>:30001/api/items
   ```

3. **Vérifier l'état de santé (liveness)** :
   ```bash
   curl http://<minikube-ip>:30001/health/live
   ```

4. **Vérifier l'état de santé (readiness)** :
   ```bash
   curl http://<minikube-ip>:30001/health/ready
   ```

## Ressources et Configuration

Les ressources de l'application sont configurées dans `backend-deployment.yaml` :
- **Mémoire requise** : 64Mi
- **Mémoire limite** : 128Mi
- **CPU requis** : 250m
- **CPU limite** : 500m

L'application est également configurée avec une **probe de liveness** et une **probe de readiness** pour vérifier l'état de santé de l'application.

## Politique Réseau

Le fichier `backend-networkpolicy.yaml` limite les connexions à la base de données, en autorisant uniquement le service `backend` à se connecter au service `database`.

## Nettoyage

Pour supprimer tous les déploiements et services :

```bash
kubectl delete -f k8s/
minikube stop
```

