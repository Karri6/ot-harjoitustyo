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
Voit nyt luoda uuden käyttäjän, tai vaihtoehtoisesti kirjautua valmiiksi luodulla testikäyttäjällä, jolle on luotu päiväkirjaan merkintöjä tarkasteltavaksi.

### Ajaa testit
```
poetry run invoke test 
```
### Ajaa testikattavuuden raportin
```
poetry run invoke coverage-report
```


### Linkki harjoitustyön tuntikirjanpitoon
[tuntikirjanpito](python-app/dokumentaatio/Tuntikirjanpito.md)

### Changelog linkki
[changelog](python-app/dokumentaatio/changelog.md)

### Sovelluksen arkkitehtuuri
[Arkkitehtuuri.md](python-app/dokumentaatio/arkkitehtuuri.md)
