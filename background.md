# CSS

## Background-color:

Per indicar el color de fons d'un element HTML utilitzem la propietat background-color.

Per exemple podem fer que una web tingui un color de fons:

```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: lightblue;
}
</style>
</head>
<body>

<h1>Hello World!</h1>

<p>This page has a light blue background color!</p>

</body>
</html>
```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-color_body)

Però podem fer que cada element del web tingui un color de fons diferente:

```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: lightblue;
}

h1 {
  background-color: lime;
}

p {
  background-color: red;
} 

</style>
</head>
<body>

<h1>Hello World!</h1>

<p>This page has a light blue background color!</p>

</body>
```

## Background-image:

Un element del web pot tenir una imatge de fons, per a fer-ho utilitzem la propietat background-image:

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image)

La imatge es pot aplicar a tot el web o a un element individual:

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image_p)

### Repetir imatge de fons:

#### Repetir horitzontalment i verticalment:

Les imatges de fons, per defecte, es repeteixen tant horitzontalment com verticalment.

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image_gradient1)

#### Repetir horitzontalment:

Podem indicar que només es repeteixi horitzontalment indicant la propietat **background-repeat: repeat-x;**

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image_gradient2)

#### Repetir verticalment:

Per repetir-la només verticalment utilitzaríem la propietat **background-repeat: repeat-y;**

#### No repetir la imatge:

Per a que una imatge no es repeteixi utilitzem la propietat **background-repeat: no-repeat;**

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image_norepeat)

Podem probar les propietats anteriors a l'exemple anterior.

#### Posició de la imatge:

Podem indicar la posició a la que volem que es dibuixi la imatge amb la propietat **background-position: right top;**

En aquesta propietat podem indicar:

![image](https://user-images.githubusercontent.com/110727546/218272870-dffa369c-4514-496b-a55b-af740bf22917.png)

Exemple:

```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-image: url("img_tree.png");
  background-repeat: no-repeat;
  background-position: right bottom;
  margin-right: 200px;
}
</style>
</head>
<body>

<h1>Hello World!</h1>
<p>Here, the background image is only shown once. In addition it is positioned away from the text.</p>
<p>In this example we have also added a margin on the right side, so that the background image will not disturb the text.</p>
<h1>Hello World!</h1>
<p>Here, the background image is only shown once. In addition it is positioned away from the text.</p>
<p>In this example we have also added a margin on the right side, so that the background image will not disturb the text.</p>
<h1>Hello World!</h1>
<p>Here, the background image is only shown once. In addition it is positioned away from the text.</p>
<p>In this example we have also added a margin on the right side, so that the background image will not disturb the text.</p>
<h1>Hello World!</h1>
<p>Here, the background image is only shown once. In addition it is positioned away from the text.</p>
<p>In this example we have also added a margin on the right side, so that the background image will not disturb the text.</p>
<h1>Hello World!</h1>
<p>Here, the background image is only shown once. In addition it is positioned away from the text.</p>
<p>In this example we have also added a margin on the right side, so that the background image will not disturb the text.</p>

</body>
</html>
```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image_position)

#### Fixar la imatge:

Podem indicar per CSS si volem que la imatge es quedi fixa en pantalla o que al fer scroll es mogui amb la resta d'elements, per a fer-ho utilitzem la propietat **background-attachment**.

- Imatge fixa:  background-attachment: fixed;
- Imatge amb scroll:  background-attachment: scroll;

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background-image_attachment2)

### Indicar totes les propietats amb un shorthand:

Per fer el codi més curt podem indicar les propietats background totes seguides amb la propietat background.

Per exemple, aquest codi:

```
body {
  background-color: #ffffff;
  background-image: url("img_tree.png");
  background-repeat: no-repeat;
  background-position: right top;
}
```

Podem indicar-ho així:

```
body {
  background: #ffffff url("img_tree.png") no-repeat right top;
}
```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_background_shorthand)

## Practicar:

[Practica](https://www.w3schools.com/css/exercise.asp?filename=exercise_background1)
