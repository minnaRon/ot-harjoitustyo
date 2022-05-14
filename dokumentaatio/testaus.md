# Testausdokumentti

Ohjelmaa on testattu automaattisilla unittest -yksikkö ja integraatiotesteillä, sekä manuaalisesti järjestelmätasoisesti.

## Yksikkö ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavia, services -hakemiston luokkia, testataan testihakemiston services -hakemistosta löytyvillä testiluokilla: 
- [TestPractiseService](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/services/practise_service_test.py) testaa 'PractiseService' -luokkaa
- [TestPractiseLoginService](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/services/practise_login_service_test.py) testaa 'PractiseLoginService' -luokkaa
- [TestUserService](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/services/user_service_test.py) testaa 'UserService' -luokkaa
- [TestWordService](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/services/word_service_test.py) testaa 'WordService' -luokkaa

Testeissä käytetään riippuvuuksien käsittelyyn pääasiassa Mock -olioita.
PractiseService -luokassa käytetään FakeRepository -luokkaa harjoiteltavien sanaparien tuomiseksi testeihin.

### Repositorio -luokat

Repositorioita, jotka löytyvät repositories -hakemistosta, testataan testihakemiston repositories -hakemistosta löytyvillä testiluokilla: [TestPractiseRepository](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/repositories/practise_repository_test.py), [TestUserRepository](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/repositories/user_repository_test.py), [TestWordRepository](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/repositories/word_repository_test.py).

Testeissä on käytössä ainoastaan testiluokan setUp -metodissa tietokantaan tallennettu syöte.

### Integraatiotestausta usean luokan yli

Lisäksi service ja repository -luokkien yhteistoimintaa testataan hieman järjestelmätestityyppisesti luokan 
[TestMultiClass](https://github.com/minnaRon/ot-harjoitustyo/blob/master/src/tests/integration_test.py) avulla.

### Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksessa haarautumakattavuus on 90%.

![](./kuvat/coverage_report.png)

## Järjestelmätestaus

Sovelluksen järjestelmätestaus suoritettiin manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla Linux -ympäristössä.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](./vaatimusmaarittely.md) ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi.
Tarkistettiin myös, että syötekentille määritellyistä vaatimuksista poikkeava syöte aiheuttaa virheilmoituksen.

Sovelluksen syötteiden vaatimuksissa on määritelty:

Rekisteröityminen -näkymässä
- tunnuksen tulee olla pituudeltaan 2-20 merkkiä ja tunnus on uniikki
- salasanakenttien salasanat vastaavat toisiaan, mikäli sellainen on annettu

Kirjautuminen -näkymässä
- tunnus on olemassa tietokannassa
- salasana annetaan, jos sellainen on annettu rekisteröitymisen yhteydessä

Sanojenlisäys -näkymässä
- valitut kielet poikkeavat toisistaan
- sanalistat eivät ole eripituiset, muuten käyttäjä voi täyttää sanakentät haluamillaan merkeillä täysin vapaasti.

Harjoittelunäkymässä
- valitaan ensin yksi vasemmanpuoleisista sanoista
