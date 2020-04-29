# Käyttäjätapaukset

## Toteutetut käyttäjätapaukset

* Normaali käyttäjä voi lisätä juoksutreeninsä tuloksen: toistot, juostun matkan ja kuluneen ajan pitääkseen kirjaa harjoitushistoriastaan. (kyselyissä yksinkertaistus result-taulun perinnästä)
```
INSERT INTO Session(account_id, date) VALUES (?, ?);
INSERT INTO Conditioning(id, session_id, distance, time) VALUES (?, ?, ?, ?);
```

* Normaali käyttäjä voi lisätä voimaharjoitusten tuloksia (liike, toistot, paino) pitääkseen kirjaa historiastaan. (kyselyissä yksinkertaistus result-taulun perinnästä)
```
INSERT INTO Session(account_id, date) VALUES (?, ?);
INSERT INTO Strength(id, session_id, reps, weight) VALUES (?, ?, ?);
```

* Normaali käyttäjä voi muokata ja poistaa tulosdataa korjatakseen kirjattaessa mahdollisesti tapahtuvia virheitä.
```
UPDATE Conditioning SET(distance=?, time=?) WHERE id=?;
```
* Normaali käyttäjä voi tarkastella analytiikkaa aktiivisuudestaan viimeisen 30 päivän ajalla nähdäkseen kuormituksensa määrän.

(sqlite)
```
SELECT COUNT(DISTINCT date) FROM session WHERE date BETWEEN date('now', '-30 days') AND date ('now', 'localtime') AND account_id = ?; 
```
(postgresql)
```
SELECT COUNT(DISTINCT date) FROM session WHERE date > current_date - interval '30' AND account_id = :id;
```
* Normaali käyttäjä näkee henkilökohtaiset voimatulosten ennätyksensä ja voi näin seurata niiden kehitystä:
```
SELECT max(date), workout.name, reps, max(weight) AS weight FROM Strength JOIN workout ON workout.id=strength.workout_id JOIN result ON strength.id=result.id JOIN session ON session.id=session_id WHERE account_id = ? GROUP BY workout.name, reps;
```
* Normaali käyttäjä näkee henkilökohtaiset juoksuennätyksensä ja voi näin seurata niiden kehitystä:
```
SELECT max(date), distance, min(time) AS time FROM Conditioning JOIN result ON conditioning.id=result.id JOIN session ON session.id=session_id WHERE account_id = ? GROUP BY distance;
```
* Ylläpitäjä näkee listan käyttäjistä ja voi näin seurata käyttäjien määrää.
```
SELECT account.id AS account_id, account.name AS account_name, account.username AS account_username, account.password_hash AS account_password_hash FROM account
```
* Ylläpitäjä näkee käyttäjien aktiivisuuden ja voi näin seurata sovelluksen käyttöastetta.
```
SELECT COUNT(*) FROM Session;
```
* Ylläpitäjä voi lisätä toiselle käyttäjälle ylläpito-oikeudet:
```
INSERT INTO UserUsergroup(account_id, usergrou_id) VALUES (?,?);
```

* Ylläpitäjä voi halutessaan poistaa käyttäjältä (ei omistajalta eli superUserilta tai itseltään) ylläpitäjän oikeudet.
```
DELETE FROM Userusergroup WHERE account_id=? AND usergroup_id=?;
```
## Käyttäjätapauksia jatkokehitykseen:

* Normaali käyttäjä näkee statistiikkaa tulostensa kehittymisestä.

* Normaali käyttäjä voi luoda viikottaisen harjoitussuunnitelman ja seurata sen toteutumista.
