## Introducció al HTML.

### Què és HTML?

![HTML](https://user-images.githubusercontent.com/110727546/211291962-53330a1b-3811-456c-93b5-59bc18e88a9b.png)

**HTML** són les sigles **de HyperText Markup Language** o, en català, Llenguatge de marques de hipervincles.

**HyperText:** Els fitxers HTML només contenen text, cada vegada que s'ha de fer servir un recurs extern, com un vídeo o una imatge, la URL del recurs s'incorpora de forma correcta al text, de forma que el navegador sigui qui uneixi els recursos.

**Markup:** Les marques a les que es refereix el nom "markup" són indicacions de contingut per a pàgines web, cada marca o tag indica quin contingut hi ha.

**Language:** És un llenguatge perquè té una semàntica (paraules clau) i una sintaxi (normes d'escriptura) que el defineixen.

Actualment anem per la versió 5 de HTML.

### D'on surgeix HTML?

![Tim](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tim_Berners-Lee.jpg/220px-Tim_Berners-Lee.jpg)

**Tim Berners-Lee** va ser el creador del primer navegador web a 1990 anomenat **worldwideweb** utilitzant el sistema NEXTSTEP i del primer servidor web anomenat **httpd** (HyperText Transfer Protocol Daemaon).

### Versions d'HTML:

1991 - Tim Berners-Lee crea el conjunt HTML 1.0. La primera versió reconeguda de HTML és de 1993.<br>
1995 - Versió HTML 2.0.<br>
1997 - Versió HTML 3.0.<br>
1999 - Versió HTML 4.0.<br>
2014 - Versió HTML 5.0 (Actual).<br>

HTML és un derivat de SGML.

### Què és SGML: 

El HTML és un derivat del llenguatge SGML ( Standard Generalized Markup Language), que és a la vegada un derivat del llenguatge GML (Generalized Markup Language) de IBM.

En realitat GML es diu així pels cognoms dels seus creadors (Goldfarb, Mosher, Lorie), després li van donar un significat.

Es tracta d'un llenguatge que serveix per definir documents sense definir la seva presentació, per exemple definint capítols, títols, seccions, etc... Però no el tamany de la lletra o el seu color. 

### Estructura d'un document HTML:

![image](https://user-images.githubusercontent.com/110727546/218274745-f79c1aaf-5e35-40f0-81ad-3734de846c06.png)


- Un document HTML està format per els tags o etiquetes.
- Tot el document va entre els tags html i /html.
- La etiqueta head serveix per tenir dins la meta informació de la pàgina web (informació sobre el contingut), a més del tag title que és el títol de la pàgina web.
- La etiqueta body serà la que tindrà els elements que conformen la pàgina web.
  - Els tags del document no són Case Sensitive, poden estar escrits en maiúscules i minúscules.
  - Els tags s'han de tancar excepte casos com br.
  
#### Exemple bàsic:

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

  ### Editor HTML:
  
  Podem utilitzar qualsevol editor de text per treballar amb HTML, però farem servir [Visual Studio Code](https://code.visualstudio.com/docs/setup/linux).
  
  ## Elements HTML (tags):

  ### Capçaleres:
  
  Els tags de capçalera són h1, h2, h3... Fins h6 (h per heading).
  
  Serveixen per canviar el tamany de lletra i identifiquen títols dins del web.
  
  ### Paràgrafs:
  
  Els tags de paràgraf identifiquen paràgrafs de text, son p.
  
  ### Links:
  
  Serveixen per escriure hipervincles que enllacen a altres webs.
  
  ```
  <a href="URL destí">Text del vincle</a>
  ```
  Es pot fer servir l'atribut target que diu on s'obrirà el vincle, per exemple target="_blank" obrirà el vincle en una pàgina nova, mentre que target="_self" l'obrirà a la mateixa.
  
  ### Images:
  
  El tag img serveix per incrustar imatges al web, per exemple: 
  
  ```
  <img src="URL de la imatge" alt="text a mostrar si no es pot mostrar la imatge" width="100" height="100"> 
  ```
  Mostrarà una imatge escalada a 100x100.
  
  ### Salt de línia: 
  
  El tag br crea un salt de línia a la pàgina.
  
  ### Formatejar text:
  
- b: Negreta.
- strong: Text important.
- i: Cursiva.
- em: Text emfatitzat.
- small: Text més petit.
- mark: Text marcat.
- del: Text tatxat.
- ins: Subratllat.
- sub: Subíndex.
- sup: Súperíndex.

### Comentaris:

Es pot comentar el text HTML (línies que no executa el navegador), amb el tag !

Exemple:

```
<!-- comentari -->
```

### Taules.

Per mostrar una taula utilitzem els tags:

- table: inici de taula.
- th: table header, resalta el text de la cel·la.
- tr: inici de Fila.
- td: Element de la taula, cel·la.
- colspan: Una cel·la ocupa més d'una columna.
- rowspan: Una cel·la ocupa més d'una fila.


Exemple:

```
<table>
  <tr>
    <td>Element1</td>
    <td>Element2</td>
    <td>Element3</td>
  </tr>
</table>
```

Exemple amb headers i columnes que ocupen més d'una columna.

```
<table>
  <tr>
    <th>Element1</th>
    <th>Element2</th>
    <th>Element3</th>
  </tr>
    <tr>
    <td colspan="2">Ocupa columna 1 i 2</td>
    <td>Ocupa columna 3</td>    
  </tr>
</table>
```

### Llistes.

Hi ha dos tipus de llistes, ordenades i desordenades.

Les desordenades utilitzen els tags ul (unordered list) i li (list item).

```
<ul>
  <li>Element1</li>
  <li>Element2</li>  
</ul>
```

Les ordenades utilitzen els tags ol (ordered list) i li (list item).

```
<ol>
  <li>Element1</li>
  <li>Element2</li>  
</ol>
```

Activitats:

1.- Fem una pàgina web anomenada Xllista.html (on X és el vostre cognom) amb una llista ORDENADA de la compra de, com a mínim, 10 elements.
Feu servir tags header al web per indicar el nom de la llista.

2.- Fem una pàgina web anomenada Xhorari.html (on X és el vostre cognom) amb una taula amb el vostre horari, feu servir negreta per indicar les hores del pati.

3.- Fem una pàgina web anomenada Xcurrículum.html (on X és el vostre cognom) amb un curriculum vitae vostre amb una foto inclosa.
Feu servir diferents tags de llistes, format de text, headers, imatge, etc.

4.- Fem una pàgina web anomenada Xpelicula.html (on X és el vostre cognom) amb la informació d'una pel·lícula que us agradi, similar a la de la imatge següent.

5.- Fem una pàgina web anomenada Xindex.html (on X és el vostre cognom) que serà un web amb links a les 4 pàgines anteriors.

![image](https://user-images.githubusercontent.com/110727546/211312288-24a7feb6-9638-4d05-b66a-7c4db9e67f6d.png)

  

