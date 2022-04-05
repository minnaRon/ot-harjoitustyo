# Ohjelmistotekniikka, harjoitustyö

## Sanastotreeni

Sovellus tulee olemaan tarkoitettu vieraskielisen sanaston harjoitteluun. Tällä hetkellä hieman alkua harjoittelunäkymästä ja sen toiminnallisuudesta testailtavissa.

## Python -versio

Sovelluksen sujuvan toiminnan kannalta Python -version tulisi olla vähintään 3.8.

## Dokumentaatio

- *käyttöohje tähän*

[vaatimusmäärittely](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/minnaRon/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- *changelog tähän*

## Asennus

1. Asenna riippuvuudet komennolla:

'''bash
poetry install
'''

2. Käynnistä sovellus komennolla:

'''bash
poetry run invoke start
'''

## Komentorivitoiminnot

### Ohjelman suorittaminen

Aloita ohjelman suoritus komennolla:

'''bash
poetry run invoke start
'''

### Testaus

Aloita testaus komennolla:

'''bash
poetry run invoke test
'''

### Testikattavuus

Testikattavuusraportin saa tuotettua komennolla:

'''bash
poetry run invoke coverage-report
'''

Raportti löytyy hakemistosta htmlcov.
