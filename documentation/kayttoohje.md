#  Käyttöohje

## Sovelluksen rakenne

Sovellus koostuu käyttäjän luomisen ja kirjautumisen lisäksi yläpalkissa näkyvistä päätoiminnoista: tulosten kirjaamisista, lisättyjen tulosten analyysista sekä käyttäjien hallinnasta, joista viimeinen on ainoastaan ylläpitäjien käytettävissä.

Kaikki sovelluksen lomakkeet validoivat syötettä niin, että syöte vastaa kysyttyä tietoa (esimerkiksi juoksutuloksen juostu matka ei voi olla alle 1 m tai yli 100 km), ja rajoitteiden rikkoutuessa sovellus antaa vastaavan virheilmoituksen.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/index.png"/>

## Päätoiminnot

## Käyttäjätilitoiminnot

### Uuden tunnuksen luominen

Sovellukseen luodaan uusi tunnus valitsemalla etusivulla (Workout Logger -tekstiä painamalla), kirjautumattomassa tilassa sivuvalikosta 'sign up'. Uusi tunnus luodaan täyttämällä lomake ja tallennetaan painikkeesta 'create new user'. Superuseria lukuun ottamatta uusi käyttäjä saa tavallisen käyttäjän oikeudet, ja laajemmat oikeudet voi antaa ainoastaan ylläpitäjä.

Käyttäjätilin luomisen jälkeen luotu käyttäjä kirjataan automaattisesti sisään.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/signup.png"/>

### Kirjautuminen sisään ja ulos

Sovellukseen kirjaudutaan etusivulla olevan sivuvalikon painikkeesta 'login', ja ulos kirjaudutaan saman valikon painikkeesta 'logout *name*' (näkyy vain kirjautuneena).

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/login.png"/>

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/logout.png"/>

## Suorituksen kirjaaminen

Seuraavat toiminnot löytyvät päävalikon välilehdeltä _Log_.

### Juoksutuloksen kirjaaminen

Juoksutulokset kirjataan välilehdellä _Log a running session_. Ensimmäisessä näkymässä lomakkeeseen täytetään tehtyjen kierrosten määrä, sekä juostu matka. Sovellus pyytää intervallien tietoja, ja normaalin juoksulenkin tapauksessa kenttään _rounds_ voidaan kirjata numero 1.

Painikkeesta _Confirm_ siirrytään toiseen näkymään, jossa on intervallien lukumäärää vastaava määrä kenttiä, joihin voidaan täyttää juoksuun kulunut aika muodossa hh:mm:ss. Tulos tallennetaan painikkeesta _create new result_.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/insertintervals.png"/>

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/insertruntimes.png"/>

### Voimatuloksen kirjaaminen

Voimatuloksia voidaan kirjata välilehdellä _Log a strength session_. Ensimmäisessä näkymässä kirjataan liike, tehdyt sarjat ja toistot, ja toisessa (siirrytään painikkeesta _Confirm_) kirjataan jokaisessa sarjassa käytetty paino. Kehonpainolla harjoiteltaessa painoksi voidaan kirjata 0. Tulokset tallennetaan painikkeesta _create new result_.

Sekä juoksu- että voimatulosta kirjattaessa uuden tuloksen luomisen jälkeen siirrytään automaattisesti viimeisimpien tulosten listaussivulle.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/insertsessionspecs.png"/>

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/insertweights.png"/>

### Kirjatun tuloksen muokkaaminen

Kaikkia kirjattuja tuloksia voidaan muokata välilehdellä _Modify recent results_. Ensimmäisellä sivulla valitaan muokattava tulos ko. tuloksen vieressä olevasta painikkeesta.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/selectmodify.png"/>

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/savemodified.png"/>

### Kirjatun tuloksen poistaminen

Kirjattu tulos voidaan poistaa valitsemalla välilehdellä _Modify recent results_ valitsemalla poistettava tulos, ja painamalla painiketta _Delete_. Mikäli poistettu tulos oli kyseisen harjoituskerran ainoa, myös merkintä harjoituskerrasta poistuu sovelluksesta automaattisesti.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/delete.png"/>

## Tulosten analysointi

Seuraavat toiminnot löytyvät päävalikon välilehdeltä _Analyze_.

### Viimeaikaiset tulokset

_Analyze_ toimintojen oletussivulla, välilehdellä _Recent results_ nähdään listaus viimeisimmistä tuloksista harjoituskerroittain. Kustakin harjoituskerrasta listataan harjoituksessa tehty liike, toistot/matka sekä aika/paino.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/listrecent.png"/>

### Juoksuennätykset

Välilehdellä _Running pb's_ nähdään käyttäjän juoksutuloksien henkilökohtaiset ennätykset matkoittain, sekä kunkin ennätyksen kirjauspäivä.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/runpbs.png"/>

### Voimaennätykset

Välilehdellä _Strength pb's_ nähdään käyttäjän voimatulosten henkilökohtaiset ennätykset. Ennätykset kirjataan liikkeittäin ja toistoittain, ja kussakin ennätyksessä mainitaan ennätyksen kirjauspäivä.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/strengthpbs.png"/>

### Aktiivisuusstatistiikka

_Activity stats_ -välilehdellä näytetään käyttäjän aktiivisuustaso harjoitus- ja lepopäivinä viimeisen kuukauden aikana, sekä aktiivisuustasona prosentteina. Aktiivisuus lasketaan kirjauspäivistä, siis usean harjoituksen kirjaaminen samana päivänä ei lisää aktiivisuutta.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/activitystats.png"/>

## Käyttäjien hallinta

Seuraavat toiminnot löytyvät päävalikon välilehdeltä _Manage users_.

Toiminnot ovat ainoastaan ylläpitäjän oikeudet saaneen käyttäjän käytettävissä. Ylläpitäjän oikeudet käyttäjä voi saada ainoastaan toisen ylläpitäjän kautta, tai luomalla käyttäjän nimellä superUser (käyttäjänimet ovat uniikkeja, joten näitä käyttäjiä voi olla vain yksi).

### Käyttäjien tarkastelu

Käyttäjien tietoja voidaan tarkastella välilehden _User stats_ alla. Sivulla käyttäjä näkee kaikkien sovellukseen kirjattujen käyttäjien nimet ja käyttäjänimet, sekä tiedon siitä, kuinka paljon harjoitusdataa sovellukseen on kokonaisuudessaan kirjattu.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/userstats.png"/>

### Käyttäjäoikeuksien muokkaaminen

Välilehdellä _Manage user rights_ ylläpitäjä voi muuttamalla 'Has admin access' -checkboxien valintaoja, kuitenkin oman käyttäjän ja omistajan (superUser) tilaa ei voida muuttaa. Muutokset tallentuvat painikkeesta _Save changes_.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/manageuserrights.png"/>
