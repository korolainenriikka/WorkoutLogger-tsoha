### Workout logger

Harjoitustyön tarkoitus on toimia treenipäiväkirjana crossfit-harjoittelussa.
Jokainen treeni sisältää useamman "workoutin" joista kirjataan voimasarjoja,
 aerobisen harjoittelun tuloksia, sekä ns. benchmark-treenejä. Kukin näistä
on oma tuloksensa, joka puolestaan viittaa treenin nimeen.

Ongelmallisin kohta nykyisessä tietokantakaaviossa on se, että tuloksia on 
useamman tyyppisiä; kysessä on joko toistot+paino, matka+aika tai tulos, mutta
 yksi result-taulu rajaa mahdollisuuksia tai se mahdollisesti sisältää 
näitä kaikkia tietotyyppejä. Siksi workout-taulussa on tieto type, joilla 
taulun oikea sisältö voidaan tarkastaa. Työhön voisi lisätä perintää ja
useammat tulostyypit, mutta tällöin työstä tulee turhan laaja. Tulosrivien määrä 
pysyy joka tapauksessa suhteellisen pienenä. 

Tarkoitus olisi saada aikaan jonkinlaista statistiikkaa sekä pysyvä
tallennuspaikka tuloksille, aiemminkin niitä on kirjattu mutta vähän minne
milloinkin, ja tietoja on mennyt paljon hukkaan, mikä on sääli.

[tietokantakaavio](https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/tshohadiagram.png)
