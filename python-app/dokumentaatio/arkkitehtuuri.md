# Sovelluksen arkkitehtuuri

## Käyttöliittymä
Sovelluksella on neljä päänäkymää sekä kaksi sivunäkymää lisätietoja varten.\
Päänäkymät ovat toteutettu omina luokkinaan ja sivunäkymät luodaan niistä käsin.\
Pääluokkien lataamisesta ja näyttämisestä vastaa luokka [app.py](../src/app.py)

#### Päänäkymät:

- Kirjautuminen
  
- Uuden käyttäjän luominen
- Kotisivu
- Uuden merkinnän/harjoituksen kirjaus

#### Sivunäkymät:
- Koko harjoitushistorian katselu
  
- Merkinnän lisätietojen lisääminen

Käyttöliittymä hakemisto sisältää näkymien lisäksi kaksi luokkaa jotka toteuttavat kotisivun graafisia elmenttejä.\
Luokka [workout_element.py](../src/gui/workout_element.py) toteuttaa laajennettavan elementin, johon talletetaan harjoituspäiväkirjan merkintäpäivä ja sisältö graafista esitystä varten.\
Luokka [pillar_chart.py](../src/gui/pillar_chart.py) toteuttaa sarakekaavion, joka laskee ja kuvaa käyttäjän harjoitukset edellisiltä kuukausilta. 

---

## Päätoiminnot
**Alla päätoimintojen sekvenssikaaviot**

### Kirjautuminen
- Käyttäjä kirjautuu olemassaolevalla tunnuksella ja salasanalla, mikäli käyttäjätunnuksella löytyy käyttäjä, hakee sovellus kyseisen käyttäjän tiedot seuraavasti:

<img width="568" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/6f4d9cb0-981a-445a-b8b6-439a219d3ffc">

> kuvassa pieni erhe, oikean alakulman history ja workout repository laatikot ovat väärinpäin, tulisi olla kuten alla olevassa kuvassa

Käyttäjä antaa sovellukselle tunnuksen sekä salasanan käyttöliittymän kautta, jotka sovellus tarkistuttaa vastaavan käyttäjän salasanan.\ 
Mikäli käyttäjää ei löydy tai salasana on väärä, palauttaa LoginHandler luokan metodi login() boolean arvon False ja kirjautuminen hylätään.\
Hyväksytyn kirjautumisen yhtyedessä ohjelma siirtyy kotisivulle ja hakee json tiedostoista käyttäjän tiedot sekä harjoitushistorian.

### Uusi käyttäjä
- Mikäli käyttäjä luo uuden tunnuksen sovellukseen, tarkistaa sovellus, ettei kyseisellä tunnuksella ole jo käyttäjää ja tämän jälkeen toiminta etenee seuraavasti:
<img width="588" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/aca57e7a-00ea-4dec-9dbc-486185bf0326">

Uuden käyttäjän luominen toimii loogisesti samoin kuin kirjautminen, käyttäjä kirjaa tiedot ja JsonManager luokan check_user() metodi joko hyväksyy tai ei hyväksy käyttäjänimeä, riippuen siitä onko sellainen jo olemassa.\ Kirjautumisen onnistuessa käyttäjä siirtyy kotisivulle ja voi toimia normaalisti sovelluksessa.

### Uusi merkintä
- Käyttäjän luodessa uuden merkinnän päiväkirjaan tapahtumaketju etenee seuraavanlailla:
<img width="548" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/60b31d97-95d7-4820-88e9-ddc7efc2ed02">


Kun käyttäjä luo sovellukseen merkintöjä hakee sovellus ensin json tiedostoista kategoriat ja niihin liittyvät liikkeet, jotka tuodaan näkymään näkyville.\
Näistä käyttäjä voi luoda omia merkintöja ja kirjata lisätietoja kunkin merkinnän yhteydessä.\ Kun käyttäjä on valmis, luodaan valituista liikkeistä ja aktiviteeteista Workout olio, joka tallennetaan json tiedostoon. Harjoituksen lisäksi käyttäjän oma json tiedosto päivitetään ja näin uusi merkintä on näkyvillä heti, kun käyttäjä siirtyy takaisin kotisivulle.

## Rakenne ja sovelluslogiikka

###  Luokkakaavio
<img width="152" alt="wod_relation" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/cbeaae83-9b11-4ba6-b179-02976a033b9e">

### Pakkauskaavio
<img width="507" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/b7b8d63e-f68f-4075-9c9a-dd3a8227386b">


<img width="607" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/43298ba3-f3dd-463f-9011-6441d1df6654">
