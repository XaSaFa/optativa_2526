# CSS

## Com insertar CSS:

Hi ha 3 maneres d'utilitzar CSS dins una pàgina web:
- CSS extern.
- CSS Intern.
- CSS Inline.

### CSS extern:

El CSS extern utilitza **un fitxer separat**, en aquell document s'indica el comportament css del web i es linka al document HTML.

Com és un fitxer extern es pot utilitzar a un o més HTML diferents, així no s'ha de copiar a cada web que volem que es vegi igual.

Exemple:

```
<html>
<head>
<link rel="stylesheet" href="mystyle.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

El document CSS, com es veu al link, es diu mystyle.css i a l'exemple serà així:

```
body {
  background-color: lightblue;
}

h1 {
  color: navy;
  margin-left: 20px;
}
```

[Exemple al web](https://www.w3schools.com/css/tryit.asp?filename=trycss_howto_external)

### CSS intern:

El codi CSS s'inclou dins de l'etiqueta STYLE **a l'etiqueta HEAD** del document:

```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  margin-left: 40px;
}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
``` 

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_howto_internal)

### CSS inline:

El CSS inline és CSS que incloem al mateix tag que volem modificar i només afecta a aquell element.

Exemple:

```
<!DOCTYPE html>
<html>
<body>

<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>

</body>
</html>
```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_howto_inline)

## Prioritat CSS:

Hi ha vegades que podem tenir diferents formes de definir CSS dins un document, la prioritat sol ser que l'última modificació és la que es veu a la web.

Exemple:

```
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="mystyle.css">
<style>
h1 {color:red;}
</style>
</head>
<body>

<h1 style="color:yellow;">This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_howto_external)

**La prioritat CSS és:  **

extern < intern < inline

## Comentaris:

Els comentaris a CSS s'indiquen així:

```
<style>
p {
  color: red; /* Set text color to red */
}
</style>
```

## Practicar:

[Practica](https://www.w3schools.com/css/exercise.asp?filename=exercise_howto1)
