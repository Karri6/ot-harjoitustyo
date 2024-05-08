# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus
Sovellus toimii *liikuntapäiväkirjana*, jonka on tarkoitus pitää kirjaa käyttäjän menneistä harjoituksista, liikuntatuokioista tai muista aktiviteeteista, joita käyttäjät kirjaa sovellukseen. 
Käyttäjä voi seurata graafisesti aktiivisuuttaan ja selata aikaisempia kirjauksiaan päänäkymässä. Käyttäjän on mahdollista lisätä manuaalisesti valiten eri harjoitusmuodoista päivän harjoitus ja sen kesto.

## Käyttäjät
Sovellus on tarkoitettu henkilökohtaiseen kirjanpitoon, eikä todennäköisesti tule tukemaan muita käyttäjärooleja kuin **normaali käyttäjä**.

## Toiminnallisuus

### Kirjautuminen (tehty)
- **Uusi**-käyttäjä_ voi luoda sovellukseen uuden käyttäjätunnuksen, sovellus tarkistaa onko käyttäjää olemassa. 
- Jos käyttäjä on olemassa, hylätään käyttäjän ehdottama käyttäjänimi ja pyydetään esittämään uusi.
- Jos käyttäjä ei ole olemassa, uuden käyttäjän luominen sallitaan.

_**Vanha**-käyttäjä_ voi kirjautua olemassa olevalla tunnuksella ja salasanallaan sisään.
> huom. projektissa ei tarvitse huolehtia tietoturvasta, täten salasanoja ei sekoiteta hash funtkiolla ja ne tallennetaan suoraan ~tietokantaan~ json-tiedostoon sellaisenaan.

### Päänäkymä (tehty)
Käyttäjä voi tarkastella menneitä tietojaan kahdessa muodossa. 
- Graafinen näkymä esittää käyttäjän aikaisempien kuukausien aktiivisuuden.
- Tekstinäkymässä käyttäjä voi selata aikaisempien aktiviteettien sisältöä tarkemmin.

Käyttäjä voi kirjata uuden aktiviteetin avaamalla kirjausnäkymän.

### Kirjausnäkymä (tehty)
Käyttäjä voi valita käyttöliittymän elementeillä uuden aktiviteetin ja kirjata tapahtumalle lisätietoja esimerkiksi harjoituksen pituuden.
> TKinter ei omaa helppoa tapaa (jos ollenkaan) tehdä drag and drop elementtejä, joten käytössä simppeli klikkaa ja vahvista napin painalluksella toimiva harjoituslistan päivittäminen


## Käyttöliittymäluonnos
Luonnoksessa on neljä näkymää, kirjautuminen, uusi käyttäjä, päänäkymä ja kirjausnäkymä. Sovelluksen flow alkaa luonnollisesi kirjautumisnäkymästä, edeten siitä käyttäjän toimintojen mukaisesti joko päänäkymään tai uuden käyttäjän luomiseen. Päänäkymän ja kirjausnäkymän välillä on mahdollista liikkua edestakaisin rajattomasti.
[Luonnoksen kuva](käyttöliittymäluonnos.png)

## Jatkokehitysideoita
Sovellusta voisi laajentaa lisäämällä siihen esimerkiksi:
- Mahdollisuuden tulostaa harjoituksen
- Mahdollisuuden kirjata päivän kehonpainoa ja seurata sen kehitystä
- Laskurin päivittäiselle ravinnon tarpeelle, riippuen liikunnan määrästä.
- Mahdollisuus vapaalle merkinnälle päiväkirjaan ilman ennalta määrätyn liikkeen valitsemista.

## Muita huomioita
- Tietokannan sijaan tiedon talletus toteutettu json tiedostoilla. 
