# Käyttöohje

## Ohjelman käynnistäminen

Ennen käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä ohjelma komennolla:

```bash
poetry run invoke start
```

## Sovelluksen käyttäminen

###Sovellus käynnistyy päänäkymään:

![](./kuvat/main.png)


### Sanoston harjoittelu ilman kirjautumista:

Sanastoa voi harjoitella myös ilman kirjautumista, siirtymällä sanaston harjoittelunäkymään painamalla ‘HARJOITTELE’ -painiketta.

![](./kuvat/practice.png)

**Sanaston harjoittelu**
- valitse ensin vasemmalta puolelta sana painamalla sanan painiketta
- valitse sitten oikealta sanan käännös painamalla käännössanan painiketta
-> tämän jälkeen sovellus kertoo näkymään ilmestyvällä viestillä:
    - jos sanat vastaavat toisiaan, ilmestyy näkymään viesti pari! 
    - jos sanat eivät vastaa toisiaan, ilmestyy näkymään viesti huti!

Takaisin päävalikkoon pääsee painamalla ‘takaisin päävalikkoon’ -painiketta

![](./kuvat/main.png)


### Tunnuksen luominen

Päänäkymässä painamalla painiketta ‘rekisteröidy’, pääsee rekisteröitymisnäkymään:

![](./kuvat/register.png)

**Tunnus luodaan** 
- syöttämällä tunnus tunnuksen syötekenttään
- salasanan voi antaa salasanan syötekenttiin, se ei kuitenkaan ole pakollinen 
    - lisätty salasana vaaditaan aina kirjautuessa
Lopuksi painetaan ‘tallenna’ -painiketta

Näkymästä voi myös siirtyä rekisteröitymättä takaisin päävalikkoon painamalla
‘takaisin päävalikkoon’ -painiketta.

Rekisteröitymisen jälkeen siirrytään suoraan päänäkymään:

### Kirjautuminen

Päänäkymässä painettaessa ‘kirjaudu’ -painiketta, pääsee kirjautumisnäkymään:

![](./kuvat/login.png)

Kirjautuessa olemassa oleva tunnus syotetään tunnuksen syötekenttään ja mahdollinen
salasana salasanan syötekenttään.
Lopuksi painetaan ‘kirjaudu’ -painiketta.

Näkymästä voi myös siirtyä kirjautumatta takaisin päävalikkoon painamalla
‘takaisin päävalikkoon’ -painiketta.

Kirjautumisesi jälkeen siirrytään suoraan päänäkymään:

![](./kuvat/loginmain.png)

### Sanaston harjoittelu kirjautuneena

Päänäkymästä voi siirtyä harjoittelunäkymään painamalla HARJOITTELE -painiketta.

![](./kuvat/loginpractice.png)

**Sanaston harjoittelu**
- valitse ensin vasemmalta puolelta sana painamalla sanan painiketta
- valitse sitten oikealta sanan käännös painamalla käännössanan painiketta
-> tämän jälkeen sovellus kertoo näkymään ilmestyvällä viestillä:
    - jos sanat vastaavat toisiaan, ilmestyy näkymään viesti pari! 
    - jos sanat eivät vastaa toisiaan, ilmestyy näkymään viesti huti!

Takaisin päävalikkoon pääsee painamalla ‘takaisin päävalikkoon’ -painiketta.
Kirjautuminen ulos painamalla 'kirjaudu ulos' -painiketta vie takaisin päävalikkoon
kirjaten käyttäjän samalla ulos sovelluksesta.
- molemmissa tapauksissa harjoittelun edistyminen tallennetaan tietokantaan.

Oikean yläkulman rastista poistuttaessa edistymistä ei tallenneta.

### Sanojen lisäys sanastoon kirjautuneena

![](./kuvat/loginmain.png)

Kirjautuneena päänäkymästä pääsee sanojen lisäys -näkymään painamalla ‘Lisää sanoja’ -painiketta.


![](./kuvat/addwords.png)

**Sanojen lisäys**
- lisää vasemman puoleiseen syötekenttään allekkain sanoja
- lisää vastaavat käännössanat oikeanpuoleiseen kenttään allekkain
- valitse sanojen kieli suomi/englanti syötekenttien yläpuolella olevilla valikoilla
- painamalla ‘TALLENNA’ -painiketta sanat tallentuvat sanastoon pysyvästi

Sanojen lisäys -näkymästä pääsee takaisin päävalikkoon painamalla ‘takaisin päävalikkoon’ -painiketta.