
CREATE TABLE Person (
    id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    prenom VARCHAR(50) NOT NULL UNIQUE,
    age INT NOT NULL
);

/*
INSERT INTO person(name, prenom, age)
VALUES ('DETTOL','Flamine',22),
	('Galliano','Lyse',21),
    (NULL,'Lana',24),
    ('Blazy','Anna',20),
    ('Rayn','Sophie',NULL)-- ,
    -- (NULL,NULL,NULL)
;
*/


/*

Supprimer les  éléments d'une table en SQL

Pour supprimer des éléments (lignes) d'une table en SQL, vous utilisez la commande **`DELETE`**.

Il existe deux manières principales de l'utiliser :

-----

## 1\. 🗑️ Supprimer des lignes spécifiques (avec condition `WHERE`)

C'est la méthode la plus courante et la plus sûre. Vous utilisez la clause **`WHERE`** pour spécifier les lignes exactes à supprimer.

**Syntaxe :**

```sql
DELETE FROM nom_de_la_table
WHERE condition_de_suppression;
```

### Exemples :

  * **Supprimer l'utilisateur avec l'ID 5 :**

    ```sql
    DELETE FROM utilisateurs
    WHERE id = 5;
    ```

  * **Supprimer tous les produits dont le stock est égal à zéro :**

    ```sql
    DELETE FROM produits
    WHERE stock = 0;
    ```

  * **Supprimer les commandes passées avant le 1er janvier 2024 :**

    ```sql
    DELETE FROM commandes
    WHERE date_commande < '2024-01-01';
    ```

-----

## 2\. 💣 Supprimer toutes les lignes (sans `WHERE`)

Si vous omettez la clause `WHERE`, la commande **`DELETE`** supprimera **toutes les lignes** de la table.

**Attention :** Cette opération est irréversible et supprime toutes les données \!

**Syntaxe :**

```sql
DELETE FROM nom_de_la_table;
```

### Alternative Rapide : `TRUNCATE TABLE`

Si votre objectif est de supprimer **toutes les lignes** de la table de manière définitive, il est souvent plus rapide d'utiliser la commande **`TRUNCATE TABLE`**.

  * **`TRUNCATE TABLE`** réinitialise également le compteur d'auto-incrémentation (`AUTO_INCREMENT`).
  * **`DELETE FROM`** (sans `WHERE`) supprime toutes les lignes, mais le compteur d'auto-incrémentation continue là où il s'était arrêté.

**Syntaxe `TRUNCATE` :**

```sql
TRUNCATE TABLE nom_de_la_table;
```

| Opération | Rôle | Vitesse | Réinitialise l'ID ? |
| :--- | :--- | :--- | :--- |
| **`DELETE` (avec `WHERE`)** | Supprimer des lignes spécifiques. | Lente | Non pertinent |
| **`DELETE` (sans `WHERE`)** | Supprimer toutes les lignes. | Lente | Non |
| **`TRUNCATE TABLE`** | Supprimer toutes les lignes. | Très rapide | Oui |
#

*/

