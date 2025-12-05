// Appel HTTP vers l'API Flask - port 8000
fetch("http://localhost:8000/items")

    // Conversion de la réponse en json
    .then(r => r.json())

    // Parcours des objets de la table items, affichage dans la liste <ul>
    .then(data => {
        const ul = document.getElementById("items");
        data.forEach(item => {
            const li = document.createElement("li");
            // ajout du nom
            li.textContent = item.name;  
            // ajout dans la page
            ul.appendChild(li);    
        });
    })
    // Recuperation des erreurs
    .catch(err => console.error("Erreur API:", err));

