#  Käyttöohje

## sovelluksen rakenne

Sovellus koostuu käyttäjän luomisen ja kirjautumisen lisäksi yläpalkissa näkyvistä päätoiminnoista: tulosten kirjaamisista, lisättyjen tulosten analyysista sekä käyttäjien hallinnasta, joista viimeinen on ainoastaan ylläpitäjien käytettävissä.

Kaikki sovelluksen lomakkeet validoivat syötettä niin, että syöte vastaa kysyttyä tietoa (esimerkiksi juoksutuloksen juostu matka ei voi olla alle 1 tai yli 100 km), ja rajoitteiden rikkoutuessa sovellus antaa vastaavan virheilmoituksen.

index

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

seuraavat toiminnot löytyvät päävalikon välilehdeltä _Log_

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

## tulosten analysointi

### viimeaikaiset tulokset

### juoksuennätykset

### voimaennätykset

### aktiivisuusstatistiikka

## käyttäjien hallinta

### käyttäjien tarkastelu

### käyttäjäoikeuksien muokkaaminen