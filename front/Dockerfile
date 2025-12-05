# Image Apache
FROM httpd:2.4-alpine

# Copie des fichiers front-end dans le dossier d'apache
COPY . /usr/local/apache2/htdocs/

# Ajout d’un utilisateur non-root 
#RUN adduser -D appuser 

# Utiliser cet utilisateur non-root pour le service apache
#USER appuser
