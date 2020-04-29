# Käyttäjätapaukset

## Toteutetut käyttäjätapaukset

* Normaali käyttäjä voi lisätä juoksutreeninsä tuloksen: toistot, juostun matkan ja kuluneen ajan pitääkseen kirjaa harjoitushistoriastaan.

SQL: INSERT INTO Session(account_id, date) VALUES (?, ?);

jokaista toistoa kohden:

INSERT INTO Result(session_id, distance, time) VALUES (?, ?, ?);

* Normaali käyttäjä voi lisätä voimaharjoitusten tuloksia (liike, toistot, paino) pitääkseen kirjaa historiastaan.

SQL:

* Normaali käyttäjä voi muokata ja poistaa tulosdataa korjatakseen kirjattaessa mahdollisesti tapahtuvia virheitä.

SQL:

* Normaali käyttäjä voi tarkastella analytiikkaa aktiivisuudestaan viimeisen 30 päivän ajalla nähdäkseen kuormituksensa määrän.

SQL: SELECT COUNT(DISTINCT date) FROM session WHERE date BETWEEN date('now', '-30 days') AND date ('now', 'localtime') AND account_id = ?; 

tämän kyselyn syntaksi on postgresql:ssä hieman eroava:

SELECT COUNT(DISTINCT date) FROM session WHERE date > current_date - interval '30' AND account_id = :id;

* Normaali käyttäjä näkee henkilökohtaiset ennätyksensä ja voi näin seurata niiden kehitystä.

SQL:

* Ylläpitäjä näkee listan käyttäjistä ja voi näin seurata käyttäjien määrää.

SQL: 

SELECT account.id AS account_id, account.name AS account_name, account.username AS account_username, account.password_hash AS account_password_hash 
FROM account

* Ylläpitäjä näkee käyttäjien aktiivisuuden ja voi näin seurata sovelluksen käyttöastetta.

SQL:

SELECT COUNT(*) from account;

SELECT COUNT(*) from session;

* Ylläpitäjä voi halutessaan lisätä käyttäjälle ylläpitäjän oikeudet.

SQL:

INSERT INTO Userusergroup(account_id, usergroup_id) VALUES (?, 2);

* Ylläpitäjä voi halutessaan poistaa käyttäjältä (ei omistajalta eli superUserilta tai itseltään) ylläpitäjän oikeudet.

SQL:

DELETE FROM Userusergroup WHERE account_id=? AND usergroup_id=2;

## Käyttäjätapauksia jatkokehitykseen:

* Normaali käyttäjä näkee statistiikkaa tulostensa kehittymisestä.

* Normaali käyttäjä voi luoda viikottaisen harjoitussuunnitelman ja seurata sen toteutumista.
