# Ohjelmistotekniikka, harjoitustyö

## Sanastotreeni

Sovellus on tarkoitettu vieraskielisen sanaston harjoitteluun. Sanaston sanoja voi harjoitella kirjautumatta harjoittelunäkymässä. Kirjautuneena käyttäjänä harjoittelun edistyminen voidaan tallentaa tietokantaan ja sanastoon on mahdollista lisätä omia sanoja sanojenlisäysnäkymässä. Sanat tallentuvat SQLite -tietokantaan. Tietokannan sanasto on Teemu Kerolan keräämää [operating systems -sanastoa](https://www.cs.helsinki.fi/group/nodes/kurssit/kj/sanasto.html).

## Python -versio

Sovelluksen sujuvan toiminnan kannalta Python -version tulisi olla vähintään 3.8.

## Dokumentaatio

[vaatimusmäärittely](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[arkkitehtuurikuvaus](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[työaikakirjanpito](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[uusin release](https://github.com/minnaRon/ot-harjoitustyo/releases/tag/loppupalautus)

[käyttöohje](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[testaus](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

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
