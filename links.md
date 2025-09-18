# HTML

## Links:

Com hem vist els links o hipervincles són enllaços a altres documents HTML o recursos com imatges, videos...

### Ruta absoluta i relativa:

Els links poden utilitzar una ruta relativa o absoluta.

- URL Absoluta: Especifiquem l'adreça sencera del document
- Exemple:

``` <a href="http://videojuegosporalimentos.org/">Videojuegos por alimentos</a> ```

-URL Relativa: És un enllaç a un fitxer local, dins del mateix equip on està la web.
- Exemple:

``` <a href="logo.jpg">Logo</a> ```
``` <a href="contacto.html">Contactar</a> ```

Si el recurs es troba a un directori, per exemple el directori imatges ho especifiquem a la ruta relativa:

``` <a href="imatges/logo.jpg">Logo</a> ```

### Link a mail:

Els links es poden fer a una adreça de correu electrònic, en aquest cas el programa gestor de correu electrònic del dispositiu crearà un mail a l'adreça especificada.

``` <a href="mailto:javiersancho@iesebre.com">Enviar mail</a> ```

### Link a telèfon:

Els links poden obrir-se des d'un dispositiu amb capacitat per fer trucades com un telèfon inteligent.

``` <a href="tel:+34977501835">Trucar</a> ```

### Títol de Link:

Podem fer que un link tingui un títol (al deixar el punter parat a sobre es mostra):

``` <a href="https://www.w3schools.com/html/" title="Videojuegos por Alimentos">Visitar web</a> ```

### Obrir el link a la mateixa web o a una pàgina nova:

Si volem obrir el link a la mateixa pàgina web afegirem l'atribut target.

```target="_self"```

Si el volem obrir a una nova pàgina web utilitzarem també l'atribut target:

```target="_blank"```

### Link a una part del mateix document:

De vegades no volem enllaçar a un nou document si no a una part del mateix document que està visitant l'usuari/a.

Per fer això hem de "marcar" un tag amb un atribut id que tingui un nom, per exemple:

``` <h2 id="seccio1"> Secció 1 </h2> ```

I el link serà així:

``` <a href="#seccio1">Anar a secció 1</a> ```

### Practicar amb links:

[Practica](https://www.w3schools.com/html/exercise.asp?x=xrcise_links1)
