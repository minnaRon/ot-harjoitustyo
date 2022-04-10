# Ohjelmistotekniikka, harjoitustyö

## Sanastotreeni

Sovellus tulee olemaan tarkoitettu vieraskielisen sanaston harjoitteluun. Tällä hetkellä alkua harjoittelunäkymästä ja sen toiminnallisuudesta testailtavissa, myös omia sanoja on mahdollista lisätä sanojen lisäysnäkymässä. Sanat tallentuvat omalla koneella SQLite -tietokantaan.

## Python -versio

Sovelluksen sujuvan toiminnan kannalta Python -version tulisi olla vähintään 3.8.

## Dokumentaatio

[vaatimusmäärittely](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

*tähän arkkitehtuurikuvauslinkki*

[työaikakirjanpito](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Aloita ohjelman suoritus komennolla:

```bash
poetry run invoke start
```

### Testaus

Aloita testaus komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin saa tuotettua komennolla:

```bash
poetry run invoke coverage-report
```

Raportti löytyy htmlcov -hakemistosta.

### Koodin laatu

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
