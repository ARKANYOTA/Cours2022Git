--!/usr/bin/env python
-- vim: set sw=4 sts=4 et fdm=marker:
--┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
--┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
--┃ Creation: 18/10/2021 15:59:51              ┃
--┃ Mise a jour: 18/10/2021 16:09:47           ┃
--┃ Fichier: TD2_sql.py                        ┃
--┃ TD       fiche 2                           ┃
--┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

-- On considère le schéma relationnel issu d’une base de données de jeu vidéo :
-- Joueurs(login : STR, mot_de_passe : STR, gold : INT, id_faction# : INT, id_metier# : INT)
-- Factions(id_faction : INT, nom_faction : STR)
-- Metiers(id_metier : INT, nom_metier : STR, lieu_travail : STR, remuneration : INT)
-- Peuples(id_peuple : INT, nom_peuple : STR)
-- Reputation(login# : STR, idPeuple# : INT, reputation : FLOAT)
-- On supposera que toutes les relations sont préalablement remplies.

-- Exercice 1 {{{
-- a) A l’aide d’une requête SQL, insérer un nouveau métier dont l’identifiant est 7, le nom est ‘Cordonnier’ le lieu de travail est ‘Atelier’ et avec une rémunération de 950.
INSERT INTO "Metiers" ("id_metier","nom_metier", "lieu_travail", "remuneration") VALUES (7, 'Cordonnier', 'Atelier', 950)
-- b) A l’aide d’une requête SQL, mettez à jour le métier de cordonnier en modifiant sa rémunération de 950 à 1200.
UPDATE "Metiers"
SET "remuneration" = 1200
WHERE nom_metier=='Cordonnier' 
--c) A l’aide d’une requête SQL, supprimez le joueur qui a pour login ‘Yphe’.
DELETE FROM "Joueurs"
WHERE login=='Yphe' 
--d) A l’aide d’une requête SQL, supprimez tous les joueurs ayant moins de 1000 golds
DELETE FROM "Joueurs"
WHERE gold<=1000 


-- Exercice 2 {{{
--1. Tous les logins des joueurs
SELECT login FROM "Joueurs"
--2. Tous les logins et mot de passe des joueurs
SELECT login, mot_de_passe FROM "Joueurs"
--3. Le nombre de golds que possède le joueur ‘Yphe’
SELECT gold FROM "Joueurs" WHERE login=='Yphe'
--4. Tous les logins et mot de passe des joueurs
SELECT login, mot_de_passe FROM "Joueurs"
--5. La somme des golds de tous les joueurs
SELECT SUM(gold) FROM "Joueurs"
--6. Les lieu de travails distincts
SELECT DISTINCT lieu_travail FROM "Metiers"
--7. Le nombre de métiers
SELECT COUNT(*) FROM "Metiers"
--8. Le nombre de métiers dont la rémunération est supérieure à 1000
SELECT COUNT(*) FROM "Metiers" WHERE remuneration>1000
--9. Les nom des factions triés par ordre alphabétique croissant
SELECT nom_faction FROM "Factions" ORDER BY nom_faction ASC
--10. La moyenne de rémunération des métiers.
SELECT AVG(remuneration) FROM "Metiers"
--11. Le login des joueurs qui ont le métier tailleur
-- SELECT login FROM "Joueurs" WHERE id_metier==(SELECT id_metier FROM "Metiers" WHERE nom_metier=='Tailleur')
SELECT login FROM Joueurs
JOIN Metiers ON Metiers.id_metiers = Joueurs.id_metier WHERE nom_metier='Tailleur'
--12. Le login des joueurs ayant pour faction ‘Mage’
-- SELECT login FROM "Joueurs" WHERE id_faction==(SELECT id_faction FROM "Factions" WHERE nom_faction=='Mage')
SELECT login
FROM Joueurs
JOIN Factions ON Faction.id_faction = Joueurs.id_faction
WHERE nom_faction='Mage'
--13. Le login des joueurs qui sont bijoutiers et qui ont plus de 1000 gold
SELECT login FROM "Joueurs" WHERE id_metier==(SELECT id_metier FROM "Metiers" WHERE nom_metier=='Bijoutier') AND gold>1000
SELECT login FROM "Joueurs" JOIN Metiers.id_metier = Joueurs.id_metier WHERE nom_metier='Bijoutier' AND gold>1000
--14. Le nombre de joueurs ayant un métier qui s’exerce dans le lieu de travail ‘Champs’
SELECT COUNT(*) FROM "Joueurs" WHERE id_metier==(SELECT id_metier FROM "Metiers" WHERE lieu_travail=='Champs')
SELECT COUNT(*) FROM "Joueurs" JOIN Metiers ON Metiers.id_metier = Joueurs.id_metier WHERE lieu_travail=='Champs'
--15. Le nombre de joueurs ayant soit plus de 2000 gold soit un métier ayant une rémunération supérieure à 2000
SELECT COUNT(*) FROM "Joueurs" WHERE gold>2000 OR id_metier==(SELECT id_metier FROM "Metiers" WHERE remuneration>2000)
SELECT COUNT(*) FROM "Joueurs" JOIN Metiers ON Metier.id_metier = Joueur.id_metier WHERE remuneration>2000 OR gold>2000
--16. La somme des golds des joueurs ayant pour faction ‘Archer’
SELECT SUM(gold) FROM "Joueurs" WHERE id_faction==(SELECT id_faction FROM "Factions" WHERE nom_faction=='Archer')
SELECT SUM(gold) FROM "Joueurs" JOIN Factions ON Factions.id_faction = Joueurs.id_faction WHERE nom_faction='Archer'
--17. Le login du joueurs ayant le plus faible niveau de réputation avec le peuple ‘Humains’
--  SELECT login FROM "Joueurs" WHERE
--  SELECT MIN(reputation) FROM "Joueurs" WHERE id_peuple==(SELECT id_peuple FROM "Peuples" WHERE nom_peuple=='Humains')
SELECT
--18. Les logins des joueurs et leur réputation par rapport aux peuple ‘Nains’
SELECT login, reputation FROM "Joueurs" WHERE id_peuple==(SELECT id_peuple FROM "Peuples" WHERE nom_peuple=='Nains')
SELECT login, reputation FROM "Joueurs"
    JOIN Reputation ON Retpuation.login = Joueurs.login
    JOIN Peuple ON Peuple.id_peuple = Reputation.id_peuple
    WHERE nom_peuple='Nains'
--19. Les logins des joueurs et leur rémunération triée par ordre décroissant
SELECT login, remuneration FROM "Joueurs"
    JOIN Metiers ON Metiers.id_metier = Joueurs.id_metier
    ORDER BY remuneration DESC
--20. Les logins, mot de passes, nom de factions et métiers des joueurs triés par login
SELECT login, mot_de_passe, nom_faction, nom_metier FROM "Joueurs"
    JOIN Factions ON Factions.id_faction = Joueurs.id_faction
    JOIN Metiers ON Metiers.id_metier = Joueurs.id_metier
    ORDER BY login ASC
--21. Le login des joueurs ayant pour faction ‘Assassin’ et comme métier ‘Paysan’
SELECT login FROM "Joueurs"
    JOIN Factions ON Factions.id_faction = Joueurs.id_faction
    JOIN Metiers ON Metiers.id_metier = Joueurs.id_metier
    WHERE nom_faction='Assassin' AND nom_metier='Paysan'
--22. Le nombre de joueurs ayant pour faction ‘Paladin’ et ayant un niveau de réputation par rapport aux peuples ‘Elfes’ inférieur à 5
SELECT COUNT(*) FROM "Joueurs"
    JOIN Factions ON Factions.id_faction = Joueurs.id_faction
    JOIN Reputation ON Reputation.login = Joueurs.login
    JOIN Peuple ON Peuple.id_peuple = Reputation.id_peuple
    WHERE nom_faction='Paladin' AND nom_peuple='Elfes' AND reputation<5
--23. La moyenne du niveau de réputation des joueurs ayant pour faction ‘Roublard’ par rapport au peuple ‘Géant’
SELECT AVG(reputation) FROM "Joueurs"
    JOIN Factions ON Factions.id_faction = Joueurs.id_faction
    JOIN Reputation ON Reputation.login = Joueurs.login
    JOIN Peuple ON Peuple.id_peuple = Reputation.id_peuple
    WHERE nom_faction='Roublard' AND nom_peuple='Géant'
--24. Les logins des joueurs ayant comme faction ‘Sorcier’ comme métier ‘Mineur’ et ayant un niveau de réputation supérieur à 5 par rapport au peuple ‘Orc’
SELECT l
