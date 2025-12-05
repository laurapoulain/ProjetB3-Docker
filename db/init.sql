-- Creation de la table items
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insertion de donnees de test
INSERT INTO items (name) VALUES ("Test A"), ("Test B"), ("Test C");
