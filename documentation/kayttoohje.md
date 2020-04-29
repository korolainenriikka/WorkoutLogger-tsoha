#  Käyttöohje

## sovelluksen rakenne

Sovellus koostuu käyttäjän luomisen ja kirjautumisen lisäksi yläpalkissa näkyvistä päätoiminnoista: tulosten kirjaamisista, lisättyjen tulosten analyysista sekä käyttäjien hallinnasta, joista viimeinen on ainoastaan ylläpitäjien käytettävissä.

Kaikki sovelluksen lomakkeet validoivat syötettä niin, että syöte vastaa kysyttyä tietoa (esimerkiksi juoksutuloksen juostu matka ei voi olla alle 1 tai yli 100 km), ja rajoitteiden rikkoutuessa sovellus antaa vastaavan virheilmoituksen.

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/tree/master/documentation/kuvat/index.png" height="400" width="600"/>

## päätoiminnot

## käyttäjätilitoiminnot

### uuden tunnuksen luominen

Sovellukseen luodaan uusi tunnus valitsemalla etusivulla (Workout Logger -tekstiä painamalla), kirjautumattomassa tilassa sivuvalikosta 'sign up'. Uusi tunnus luodaan täyttämällä lomake ja tallennetaan painikkeesta 'create new user'. Superuseria lukuun ottamatta uusi käyttäjä saa tavallisen käyttäjän oikeudet, ja laajemmat oikeudet voi antaa ainoastaan ylläpitäjä.

Käyttäjätilin luomisen jälkeen luotu käyttäjä kirjataan automaattisesti sisään.

signup

### kirjautuminen sisään ja ulos

Sovellukseen kirjaudutaan etusivulla olevan sivuvalikon painikkeesta 'login', ja ulos kirjaudutaan saman valikon painikkeesta 'logout *name*' (näkyy vain kirjautuneena).

login logout

## suorituksen kirjaaminen

Seuraavat toiminnot löytyvät päävalikon välilehdeltä _Log_.

### juoksutuloksen kirjaaminen

Juoksutulokset kirjataan välilehdellä _Log a running session_. Ensimmäisessä näkymässä lomakkeeseen täytetään tehtyjen kierrosten määrä, sekä juostu matka. Sovellus pyytää intervallien tietoja, ja normaalin juoksulenkin tapauksessa kenttään _rounds_ voidaan kirjata numero 1.

Painikkeesta _Confirm_ siirrytään toiseen näkymään, jossa on intervallien lukumäärää vastaava määrä kenttiä, joihin voidaan täyttää juoksuun kulunut aika muodossa hh:mm:ss. Tulos tallennetaan painikkeesta _create new result_.

insertintervals insertruntimes

### voimatuloksen kirjaaminen

Voimatuloksia voidaan kirjata välilehdellä _Log a strength session_. Ensimmäisessä näkymässä kirjataan liike, tehdyt sarjat ja toistot, ja toisessa (siirrytään painikkeesta _Confirm_) kirjataan jokaisessa sarjassa käytetty paino. Kehonpainolla harjoiteltaessa painoksi voidaan kirjata 0. Tulokset tallennetaan painikkeesta _create new result_.

Sekä juoksu- että voimatulosta kirjattaessa uuden tuloksen luomisen jälkeen siirrytään automaattisesti viimeisimpien tulosten listaussivulle.

insertsessionspecs insertweights

### kirjatun tuloksen muokkaaminen

Kaikkia kirjattuja tuloksia voidaan muokata välilehdellä _Modify recent results_. Ensimmäisellä sivulla valitaan muokattava tulos ko. tuloksen vieressä olevasta painikkeesta.

savemodified selectmodify

### kirjatun tuloksen poistaminen

Kirjattu tulos voidaan poistaa valitsemalla välilehdellä _Modify recent results_ valitsemalla poistettava tulos, ja painamalla painiketta delete. Mikäli poistettu tulos oli kyseisen harjoituskerran ainoa, myös merkintä harjoituskerrasta poistuu sovelluksesta automaattisesti.

KUVA

## tulosten analysointi

Seuraavat toiminnot löytyvät päävalikon välilehdeltä _Analyze_.

### viimeaikaiset tulokset

_Analyze_ toimintojen oletussivulla, välilehdellä _Recent results_ nähdään listaus viimeisimmistä tuloksista harjoituskerroittain. Kustakin harjoituskerrasta listataan harjoituksessa tehty liike, toistot/matka sekä aika/paino.

KUVA

### juoksuennätykset

Välilehdellä _Running pb's_ nähdään käyttäjän juoksutuloksien henkilökohtaiset ennätykset matkoittain, sekä kunkin ennätyksen kirjauspäivä.

KUVA

### voimaennätykset

Välilehdellä _Strength pb's_ nähdään käyttäjän voimatulosten henkilökohtaiset ennätykset. Ennätykset kirjataan liikkeittäin ja toistoittain, ja kussakin ennätyksessä mainitaan ennätyksen kirjauspäivä.

KUVA

### aktiivisuusstatistiikka

_Activity stats_ -välilehdellä näytetään käyttäjän aktiivisuustaso harjoitus- ja lepopäivinä viimeisen kuukauden aikana, sekä aktiivisuustasona prosentteina. Aktiivisuus lasketaan kirjauspäivistä, siis usean harjoituksen kirjaaminen samana päivänä ei lisää aktiivisuutta.

KUBAAA

## käyttäjien hallinta

Seuraavat toiminnot löytyvät päävalikon välilehdeltä _Manage users_.

Toiminnot ovat ainoastaan ylläpitäjän oikeudet saaneen käyttäjän käytettävissä. Ylläpitäjän oikeudet käyttäjä voi saada ainoastaan toisen ylläpitäjän kautta, tai luomalla käyttäjän nimellä superUser (käyttäjänimet ovat uniikkeja, joten näitä käyttäjiä voi olla vain yksi).

### käyttäjien tarkastelu

Käyttäjien tietoja voidaan tarkastella välilehden _User stats_ alla. Sivulla käyttäjä näkee kaikkien sovellukseen kirjattujen käyttäjien nimet ja käyttäjänimet, sekä tiedon siitä, kuinka paljon harjoitusdataa sovellukseen on kokonaisuudessaan kirjattu.

KUVE

### käyttäjäoikeuksien muokkaaminen

Välilehdellä _Manage user rights_ ylläpitäjä voi muuttamalla 'Has admin access' -checkboxien valintaoja, kuitenkin oman käyttäjän ja omistajan (superUser) tilaa ei voida muuttaa. Muutokset tallentuvat painikkeesta _Save changes_.

KuVvee
