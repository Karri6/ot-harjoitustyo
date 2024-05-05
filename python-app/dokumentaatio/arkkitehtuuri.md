# Sovelluksen arkkitehtuuri

### Käyttöliittymä
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

###  Luokkakaavio
<img width="152" alt="wod_relation" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/cbeaae83-9b11-4ba6-b179-02976a033b9e">

### Pakkauskaavio
<img width="494" alt="arkkitehtuuri2" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/cf7f61e0-bdf7-4cbf-b64d-86fee95f4af7">

### Sekvenssikaavio kirjautuminen
<img width="558" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/79c96ac9-bbb5-49ca-b33e-1e388ecab014">

> kuvassa pieni erhe, oikean alakulman history ja workout repository laatikot ovat väärinpäin, tulisi olla kuten alla olevassa kuvassa

### Sekvenssikaavio uusi käyttäjä
<img width="686" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/e2390287-2fab-406f-9b44-e09b7452452c">

### Sekvenssikaavio uusi merkintä
<img width="574" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/fea666a7-2a2f-4b47-86b1-09ad4e861205">
