# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenteena on kolmitasoinen kerrosarkkitehtuuri.

**Koodin pakkausrakenne:**

![Pakkausrakenne](./kuvat/packages.png)

Pakkaus ui sisältää käyttöliittymästä vastaavan koodin.

Pakkaus services sisältää sovelluslogiikasta vastaavan koodin.

Pakkaus repositories sisältää tietojen pysyväistallennuksesta vastaavan koodin.

Pakkaus entities sisältää sovelluksen tietokohteita kuvastavat luokat.


## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat Person, Practice ja Word
kuvaten käyttäjää, sanaparin harjoittelun edistymistä ja yksittäistä sanaa.

![Entiteetit](./kuvat/entities.png)

**Toiminnallisista kokonaisuuksista vastaavat luokat:**

PracticeService tarjoten metodit luokkien UI ja PractiseView toiminnoille.

UserService tarjoten metodit luokkien MainView, RegisterView ja LoginView toiminnoille.

WordService tarjoten metodit luokan AddWordsView toiminnoille.

![Pakkaukset_ja_luokat](./kuvat/packages_and_classes.png)


## Luokkakaavio

![](./kuvat/sanastotreeni_ULM.png)

## Sekvenssikaavio 

![](./kuvat/word_pair.png)
