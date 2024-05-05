# Käyttöohje

Kun olet saanut ohjelman toimimaan, seuraa näitä ohjeita. [ReadMe](../../README.md) tiedostossa on ohjeet ohjelman alustamiselle.
---
## Kirjautuminen
Sovelluksen kokonaisvaltaisen testaamisen mielessä kannattaa kirjautua sisään valmiiksi luodulla **testikäyttäjällä**.\
Testikäyttäjälle on luotu päiväkirjaan merkintöjä ja tiedostoja tarkasteltavaksi, joka havainnollistaa koko sovelluksen toiminnallisuutta.\
Vaihtoehtoisesti voit luoda oman **uuden käyttäjän** ja aloittaa tyhjältä alustalta.

- Testikäyttäjän käyttäjänimi on: 'esimerkki'
  
- Ja salasanana toimii: '1234'
- Testikäyttäjälle on luotu joitain päiväkirjamerkintöjä huhtikuulle ja sarakekaavion havainnollistamisen vuoksi litannia tyhjiä tiedostoja maalis- sekä helmikuulle.
- HUOM! Mikäli sovellusta käyttää testikäyttäjällä toukokuussa, näyttää sarakekaavio vain edellisen kahden kuukauden merkintöjä. Toukokuulle on siis itse lisättävä uusia merkintöjä. 
  > huomaa myös: Tiedostojen nimet eivät vastaa sovelluksen generoimia tiedostonimiä aivan 1:1 suhteen niiden manuaalisen muokkaamisen takia.
---
## Sovelluksen toiminta

Sovellus on tehty mahdollisimman yksiselitteiseksi tkinterin tarjoamilla työkaluilla. 
1. Kirjautumisen jälkeen käyttäjälle aukeaa päänäkymä, jossa on yhteenveto käyttäjän harjoitushistoriasta ja graafinen sarakekaavio näkymä joka visualisoi aikaisempien harjoitusten frekvenssiä.
   
2. Päänäkymässä käyttäjä voi avata aikaisempien harjoitusten sisältöä, avata koko harjoitushistorian erilliseen ikkunaan tai siirtyä lisäämään uuden merkinnän.
3. Uuden merkinnän/harjoituksen lisääminen:
   - Käyttäjä voi selata ja valita dropdown valikosta sopivimman kategorian josta etsiä harjoitusta varten liikkeitä/aktiviteettejä.
   - Mieluisan aktiviteetin löytyessä käyttäjä valitsee sen listanäkymästä ja siirtyy painamaan lisää harjoitukseen nappia.
   - Tämä vahvistaa liikkeen/aktiviteetin lisäämisen ja avaa muistiinpano näkymän, johon käyttäjä voi kirjata esimerkiksi juoksulenkin keston tai penkkipunnerrus-sarjan toistot
   - Kun käyttäjä on lisännyt haluamansa liikeet harjoitukseen, siirtyy hän painamaan tallenna harjoitus nappia, joka luo harjoituksesta json tiedoston ja lisää sen harjoitushistoriaan.
4. Kun käyttäjä on valmis voi hän sulkea sovelluksen X ikkunan painikkeella.
