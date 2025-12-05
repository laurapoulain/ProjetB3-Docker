#!/bin/bash

echo "- Build des images -"
docker compose build --no-cache

echo "- Vérification du fichier Compose -"
docker compose config

echo "- Activation de Docker Content Trust -"
export DOCKER_CONTENT_TRUST=1

echo "- Connexion au registre -"
docker logout
docker login

echo "- Push des images signées -"
docker push poulain-laura-td-docker-api:latest
docker push poulain-laura-td-docker-front:latest

echo "- Déploiement -"
docker compose down
docker compose up -d

