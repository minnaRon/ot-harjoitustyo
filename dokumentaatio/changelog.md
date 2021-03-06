# Changelog

## Viikko 1

- Sanaharjoittelutoiminnallisuutta aloiteltu
- Sovelluksen perusajatuksen voi nähdä ja kokeilla harjoittelu -näkymässä
- Lisätty virtuaaliympäristön asetukset
- Lisätty tietokannaksi SQLite
- Lisätty tkinter graafista käyttöliittymää varten
- Lisätty sovelluksen käynnistysohjeet ja task käynnistykseen sekä testaukseen
- Lisätty UI, MainView ja PractiseView -luokat graafiselle käyttöliittymälle
- Lisätty PractiseService -luokka vastaamaan sovelluslogiikan koodista
- Lisätty luokka TestPractiseService ja muutama testi

## Viikko 2

- Sanaharjoittelutoiminnallisuuteen lisätty yhteys tietokantaan
- Sanoja voi harjoitella harjoittelu -näkymässä
- Sanojen lisäystoiminnallisuus käytettävissä
- Sanat tallentuvat tietokantaan
- Lisätty GitHubiin tietokanta, jossa harjoiteltavia sanoja on valmiina
- Lisätty AddWordsView -luokka graafiselle käyttöliittymälle
- Lisätty PractiseRepository ja WordRepository -luokat tiedon hakuun ja tallennukseen
- Lisätty testiluokka TestWordService
- Lisätty testiluokkiin testejä
- Lisätty arkkitehtuuri.md, jossa sovelluslogiikan kannalta oleelliset luokat
- Lisätty formatointiin ja koodin laadun testaukseen autopep8 ja taskeja

## Viikko 3

- Rekisteröitymisominaisuus käytettävissä, käyttäjän tiedot tallennetaan tietokantaan
- Sovellukseen voi kirjautua ja päänäkymässä voi kirjautua sovelluksesta ulos
- Kirjautuneella ja kirjautumattomalla käyttäjällä on päänäkymässä valittavissa erilaiset toiminnallisuudet
- Kirjautuneen käyttäjän harjoittelun edistymistä seurataan
- Harjoittelun edistyminen tallentuu tietokantaan ja vaikuttaa harjoiteltavaksi tuotavaan sanastoon
- Sanaston sanojen lisäystoiminnallisuus siirretty vain kirjautuneen käyttäjän käyttöön
- Lisätty luokat LoginView, RegisterView, UserService, UserRepository ja Person käyttäjien hallintaan
- Lisatty tietokantaan taulu Persons käyttäjien tallentamiseen
- Lisätty luokka Practice yksittäisen sanaparin harjoittelun edistymisen seurantaan
- Lisätty tietokantaan taulu Practices harjoittelun edistymisen tallentamiseen sanaparitasolla
- Lisätty testiluokka TestUserService ja muutama testi
- Lisätty sekvenssikaavio kuvaten sanaparin lisäämisen

## Viikko 4

- Harjoittelunäkymässä voi kirjaudu ulos, jolloin automaattisesti harjoittelun edistyminen tallennetaan ja siirrytään päänäkymään
- Kirjautumis- ja rekisteröitymisnäkymistä pääsee 'takaisin päävalikkoon' -painikkeella takaisin päänäkymään
- Lisätty testejä luokille PractiseRepository, UserRepository, PractiseService, UserService, WordService
- Lisätty docstringit luokkiin PractiseRepository, UserRepository, WordRepository, PractiseService, UserService, WordService, Person, Practice ja Word
- Lisätty tiedostoon arkkitehtuuri.md pakkauskaavio, pakkaus- ja luokkakaavio sekä loogisen tietomallin kaavio
- Lisätty tiedosto kayttoohje.md

## Viikko 5

- Harjoittelunäkymässä näkyy kirjautuneen käyttäjän harjoittelun edistyminen
- Harjoittelunäkymässä voi kirjautunut käyttäjä resetoida edistymisensä sen hetkisen harjoittelukerran osalta tai poistaa kaiken tallennetun edistymisen myös tietokannasta
- Lisätty sanapainikkeille sanojen vaihtuminen tkinterin StringVar -muuttujien kautta
- Siirretty PractiseService -luokasta kirjautuneen käyttäjän logiikka PractiseLoginService -luokkaan
- Lisätty style-konfigurointi UI -luokkaan ja näkymäluokkiin näkymien layout
- Vaihdettu uuden layoutin mukaiset kuvat kayttoohje.md -tiedostoon
- Lisätty tunnuksen validointi 2-20 merkin pituiseksi
- Lisätty testejä ja testiluokat TestPractiseLoginService, TestMultiClass
- Lisätty testaus.md
