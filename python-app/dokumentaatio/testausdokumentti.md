# Testaus

Ohjelma testattu pytest testein jotka löytyvät [testit](../src/tests) kansiosta. Lisäksi ohjelmaa testattu manuaalisesti.

## Testien laajuus

### Coverage report
Testien kattavuusraportti:\
<img width="588" alt="image" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/7c60f54b-dc97-43c5-b8f9-686d5d4af133">

Ohjelman sovelluslogiikka on testattu täysin, poislukien main.py, joka alustaa ohjelman. Käyttöliittymäluokkia, sekä app.py luokkaa joka pitää huolen näkymän vaihtumisesta ei ole testattu kuin manuaalisesti. Eli ilman näitä haarautumakattavuus 100%.

### JsonManagerTest
Huolehtii luokan testaamisesta, sekä varmistaa, että DATA hakemistosta haetaan oikeat tiedostot.

### LoginHandlerTest
Huolehtii luokan testaamisesta

### SessionManagerTest
Varmistaa, että oikea käyttäjä tallennetaan nykyiseksi käyttäjäksi

## Sovellukseen jääneet ongelmat
- Ei tarkista syötteiden sisältöä tai laajuutta
- Ei automaattista tallennusta
- Ei suurempaa virheiden käsittelyä
- Kömpelö käyttöliittymä
- Käyttöliittymän ulkoasu, käyttöympäristöstä riippuen käyttöliittymän olemus muuttuu hieman. Alla esimerkit Linux ja Windows pohjaisilla koneilla.

#### Windows:

---
<img width="512" alt="windows-run" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/f6300029-1408-4527-a8ea-0dda0bd63d89">


#### Linux:
---
<img width="355" alt="linux-run" src="https://github.com/Karri6/ot-harjoitustyo/assets/126342259/0ab9b994-4a60-4808-b3c5-e0789a066220">
