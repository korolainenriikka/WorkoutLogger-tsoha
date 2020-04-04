### ohjaaja:

sovelluksen tietokantatoiminnallisuudet eivät toimi tällä hetkellä herokussa, sillä postgresql ei suorita tietokantakomentoja samaan tapaan kuin paikallinen ohjelma (esimerkiksi lisää id-riviin nullin ja aiheuttaa errorin "not null constraint failed")

ongelma on todennäköisesti riippuvuuksissa (latasin aiemmin suuren määrän tarpeettomia, herokussa toimimattomia riippuvuuksia vahingossa, eli pip freeze ei ole käytettävissä), mutta niiden korjaus ei ollut ajan puitteissa mahdollista.

mikäli on siis mahdollista, että ohjaaja pystyy/jaksaa kokeilla ohjelmaa paikallisesti, se auttaisi sovelluksen kehitystä eteenpäin!

### Workout logger

Harjoitustyönä on treenipäiväkirja, jolla pidetään kirjaa crossfit-tyylisen harjoittelun tuloksista, siis mm. voima- ja kestävyystuloksista, ja tekee niistä statistiikkaa.

## toiminnallisuudet
### nykyiset toiminnallisuudet

Nykyisessä versiossa on rekisteröitymis- ja kirjautumistoiminnallisuudet, sekä kirjautuneena mahdollisuus lisätä, muokata ja poistaa tekstimuotoisia tuloksia. Lisäksi käytössä on salasanojen suojaus ja tietokantamigraatio.

### seuraavat muutokset

Seuraavassa versiossa voidaan lisätä loggeriin kokonainen harjoitus niin, että kukin tehty asia (esim voimasetti tai juoksuharjoitus) lisätään tekstimuotoisena tuloksena. Lisäksi sovellukseen voi rekisteröityä sekä kirjautua, ja kirjautuneena käyttäjä näkee tekemänsä tulokset. Tulokset ovat myös muokattavissa ja poistettavissa.

Yhteenvetokyselynä sovelluksessa on analytiikka-sivu, jolla käyttäjä voi valita haluamansa ajanjakson, ja näkee, kuinka monena päivänä on harjoitellut ko. ajanjakson aikana.

[viikon 4 tietokantakaavio](https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/week4Diagram.png)

### jatkokehitys

Valmiissa sovelluksessa on tulosten kirjaamiseen laajasti lisää toiminnallisuuksia: tuloksella on tyypit strength, conditioning, sekä benchmark, ja näitä tuloksia lisätessä voidaan kirjata esim. nostettuja painoja ja juoksutreenien aikoja. 

Ajan puitteissa tuotetaan lisää yhteenvetokyselyihin perustuvaa analytiikkaa, esim. henkilökohtaisia ennätyksiä sekä graafeja, jotka visualisoivat kehitystä.

Sovellukseen toteutetaan myös ylläpitäjä-käyttäjätyyppi. Ylläpitäjä näkee kaikkien käyttäjien tulokset ja aktiivisuuden, ja voi halutessaan muokata ja poistaa käyttäjiä.

[valmiin version tietokantakaavio](https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/finalDiagram.png)

## Testikäyttäjätunnus:
* username: testikayttis
* password: koirapuisto



[käyttäjätapaukset](https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/user_stories.md)

[heroku](https://workoutlogger-tsoha.herokuapp.com/)
