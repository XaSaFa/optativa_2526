# CSS

El CSS (Cascading Style Sheets) serveix per afegir estils diferents als elements HTML.

Exemple de diferents CSS aplicats al mateix codi HTML:

[Exemple](https://www.w3schools.com/css/css_intro.asp)

## Síntaxi de CSS:

Les propietats CSS sempre van en parells propietat:valor i separats per punt i coma:

![image](https://user-images.githubusercontent.com/110727546/216942534-f01e6218-8fba-49ca-afb6-c250391e031c.png)

## Selectors:

Els selectors indiquen (seleccionen) quins elements HTML es veuen alterats amb el codi CSS.

De moment utilitzarem els selectors simples:

### Selector d'element:

Els elements del tipus específicat es veuen afectats a tot el document, exemple:

```
p {
  color: red;
} 
```

Aquí indiquem que tots els elements p (paràgraf es mostraran amb color vermell, es poden combinar diferents elements:

```
h1, p {
  color: red;
} 
```

Ara afecta també als elements h1.

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_syntax_element)

### Selector per id:

Afegim l'atribut id a algun element de la pàgina i modifiquem només l'element amb aquell id:

```
<html>
  <head>
    <style>
      #para1 {
        text-align: center;
        color: red;
      }
    </style>
  </head>
  <body>
    <p id="para1">Hello World!</p>
    <p>Bye World!</p>
  </body>
</html>
```

Aquí l'estil només afecta al text Hello World!

Hem d'indicar el nom de l'id amb un coixinet **#**.

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_syntax_id)

### Selector per classe:

De vegades volem que diferents elements es comportin igual, llavors assignem un atribut class que els identifica com membres d'una classe:

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_syntax_class)

Per identificar que volem modificar el comportament d'una classe afegim un punt **.** davant del nom de la classe.

Exemple:

```
<!DOCTYPE html>
<html>
<head>
<style>
.center {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<h1 class="center">Red and center-aligned heading</h1>
<p class="center">Red and center-aligned paragraph.</p> 

</body>
</html>
```

Podem modificar només alguns elements de la classe indicant l'element a modificar davant del punt i nom de la classe:

![image](https://user-images.githubusercontent.com/110727546/216945587-2c99a2d6-3124-48b1-bf29-c5184c64a19f.png)

Aquest codi només modifica els elements p que siguin de la classe center.

També podem indicar que un element pertany a més d'una classe al seu atribut class:

![image](https://user-images.githubusercontent.com/110727546/216945760-6dc56bcd-5fb9-4200-81a1-63307706948b.png)

Aquest element pertany a les classes center i large.

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_syntax_element_class2)


## Practicar:

[https://www.w3schools.com/css/exercise.asp?filename=exercise_selectors1](https://www.w3schools.com/css/exercise.asp?filename=exercise_selectors1)





