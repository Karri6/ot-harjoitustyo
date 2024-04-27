## Ohjelmistotekniikka, harjoitustyö 

# Liikuntapäiväkirja
Kurssilla toteutetaan harjoitustyönä projekti, jonka aiheeksi olen valinnut **liikunta/harjoittelu -päiväkirja**. 
Käyttäjä voi luoda sovellukseen oman tunnuksen, seurata omaa harjoitteluaan, luoda uusia kirjauksia liikuntatapahtumista ja merkitä muistiinpanoja.

Projekti toteutetaan Python kielellä hyödyntäen yksinkertaista tkinter käyttöliittymää.
> projektin Python versio on 3.8

## Sovelluksen ajaminen

Kloonaa tämä repositorio tai lataa python app kansio kokonaisuudessaan.
> Oletuksena on, että käyttäjällä on valmiudet suorittaa poetry komentoja.

### Ajaa ohjelman
```
poetry run invoke start 
```
- Riippuen käyttäjän henkilökohtaisen järjestelmän **python** ympäristömuuttujan konfiguroinnista, saattaa ohjelman käynnistäminen ilmoittaa:

```
Pythonia ei löytynyt.
```
Tämän voi korjata vaihtamalla tasks.py tiedoston start funktion oikean python kutsun, esim *'python3'* tai *'py'*.
```
# tasks.py rivit 7-9, muokkaa komentoa tarpeen mukaan.

@task
def start(c):
    c.run("python src/main.py") 
```

Sovelluksen pitäisi nyt toimia ja voit luoda uuden käyttäjän, jolla kirjautua sisään. Vaihtoehtoisesti voit kirjautua valmiiksi luodulla testikäyttäjällä, jolle on luotu päiväkirjaan merkintöjä tarkasteltavaksi.

## Sovelluksen toiminta

Sovellus on tehty mahdollisimman yksiselitteiseksi tkinterin tarjoamilla työkaluilla. 
1. Kirjautumisen jälkeen käyttäjälle aukeaa päänäkymä, jossa on yhteenveto käyttäjän harjoitushistoriasta ja graafinen näkymä joka visualisoi aikaisempien harjoitusten frekvenssiä.
2. Päänäkymässä käyttäjä voi avata aikaisempien harjoitusten sisältöä ja/tai siirtyä lisäämään uuden merkinnän.
3. Uuden harjoituksen lisääminen:
   - Käyttäjä voi selata ja valita dropdown valikosta sopivimman kategorian josta etsiä harjoitusta varten liikkeitä/aktiviteettejä.
   - Mieluisan aktiviteetin löytyessä käyttäjä valitsee sen listanäkymästä ja siirtyy painamaan lisää harjoitukseen nappia.
   - Tämä vahvistaa liikkeen/aktiviteetin lisäämisen ja avaa muistiinpano näkymän, johon käyttäjä voi kirjata esimerkiksi juoksulenkin keston tai penkkipunnerrus-sarjan toistot
   - Kun käyttäjä on lisännyt haluamansa liikeet harjoitukseen, siirtyy hän painamaan tallenna harjoitus nappia, joka luo harjoituksesta json tiedoston ja lisää sen harjoitushistoriaan.
4. Kun käyttäjä on valmis voi hän sulkea sovelluksen X ikkunan painikkeella.

## Muut komennot

### Testit
```
poetry run invoke test 
```
### Testikattavuuden raportti
```
poetry run invoke coverage-report
```


### Linkki harjoitustyön tuntikirjanpitoon
[tuntikirjanpito](python-app/dokumentaatio/Tuntikirjanpito.md)

### Changelog linkki
[changelog](python-app/dokumentaatio/changelog.md)

### Sovelluksen arkkitehtuuri
[Arkkitehtuuri.md](python-app/dokumentaatio/arkkitehtuuri.md)
