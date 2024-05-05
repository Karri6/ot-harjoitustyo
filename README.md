## Ohjelmistotekniikka, harjoitustyö 

# Liikuntapäiväkirja
Kurssilla toteutetaan harjoitustyönä projekti, jonka aiheeksi olen valinnut **liikunta/harjoittelu -päiväkirja**. 
Käyttäjä voi luoda sovellukseen oman tunnuksen, seurata omaa harjoitteluaan, luoda uusia kirjauksia liikuntatapahtumista ja merkitä muistiinpanoja.

Projekti toteutetaan Python kielellä hyödyntäen yksinkertaista tkinter käyttöliittymää.
> projektin Python versio on 3.8

## Sovelluksen käynnistys ja käyttö

Kloonaa tämä repositorio tai lataa [python-app](python-app) kansio kokonaisuudessaan.
> Oletuksena on, että käyttäjällä on valmiudet suorittaa poetry komentoja.

### Lataa ja asenna riippuvuudet komennolla 
```
poetry install
```

### Ohjelman käynnistys
Seuraava komento käynnistää ohjelman
```
poetry run invoke start 
```
- Riippuen käyttäjän henkilökohtaisen järjestelmän **python** ympäristömuuttujan konfiguroinnista, saattaa ohjelman käynnistäminen ilmoittaa:

```
Pythonia ei löytynyt.
```
Tämän voi korjata vaihtamalla tasks.py tiedoston start funktioon oikean python kutsun, esim *'python3'* tai *'py'*.
```
# tasks.py rivit 7-9, muokkaa komentoa tarpeen mukaan.

@task
def start(c):
    c.run("python src/main.py") 
```

Sovelluksen pitäisi olla nyt käytettävissä. Seuraa [käyttöohjeita](python-app/dokumentaatio/käyttöohje.md) sovelluksen navigoimiseksi.

## Muut komennot
### Testit
Ajaa pytest testit
```
poetry run invoke test 
```
### Testikattavuuden raportti
Ajaa coverage_report komennon ja tulostaa tulokset index.html tiedostoon
```
poetry run invoke coverage-report
```
### Pylint raportti
Luo analyysin koodin laadusta
```
poetry run invoke lint
```
---
## Linkit

### Käyttöohje
- [Käyttöohje](python-app/dokumentaatio/käyttöohje.md) 

### Linkki harjoitustyön tuntikirjanpitoon
- [Tuntikirjanpito](python-app/dokumentaatio/Tuntikirjanpito.md)

### Changelog
- [Changelog](python-app/dokumentaatio/changelog.md)

### Sovelluksen arkkitehtuuri
- [Arkkitehtuuri.md](python-app/dokumentaatio/arkkitehtuuri.md)

