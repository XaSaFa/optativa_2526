# CSS

## Color

Quan estem fent webs és important conèixer els colors amb els que comptem i com indicar-los al navegador.

Tots els colors que podem interpretar amb els nostres ulls són una barreja de tres colors primaris RGB (Red, Green, Blue).

Així tots els colors que podem interpretar sempre tindran aquests tres components:

Red:

![image](https://user-images.githubusercontent.com/110727546/216930088-9a58b404-7efe-4bf7-9376-962b216ca011.png)

Green (Lima):

![image](https://user-images.githubusercontent.com/110727546/216930290-6bff1c26-2a8b-45e4-834a-e6a5b976e956.png)

Blue: 

![image](https://user-images.githubusercontent.com/110727546/216929964-2332fa0e-e1b5-491e-95ea-c14c92da47ba.png)

Blanc (tots els colors):

![image](https://user-images.githubusercontent.com/110727546/216930398-0516f51f-5f39-47ae-84e3-2ab7ace9e5c4.png)

Negre (absència de colors):

![image](https://user-images.githubusercontent.com/110727546/216930498-aaf8fbeb-019d-434f-989f-9252c9a4de0a.png)

### Colors per nom:

Hi ha una serie de 140 colors amb un nom predefinit, solen ser colors molt utilitzats.

[Llistat de colors predefinits per nom.](https://www.w3schools.com/colors/colors_names.asp)

### Colors per components:

També podem generar altres colors modificant els tres colors primaris.

![image](https://user-images.githubusercontent.com/110727546/216931040-7e47b341-ac19-4d76-a41e-a9b0b720e2f0.png)

[Barrejador de colors](https://www.w3schools.com/colors/colors_rgb.asp)

[Seleccionador de colors](https://www.w3schools.com/colors/colors_picker.asp)

### Altres models de generació de colors:

Existeixen molts altres models de catalogació dels colors, com per exemple HSL (Hue, Saturation, Lightness).

[Model HSL](https://es.wikipedia.org/wiki/Modelo_de_color_HSL)

## Color de text:

El color del text s'indica amb la propietat color, per exemple: 

```
<p style="color:blue;">color de text blau</p>
```

## Color de fons:

El color de fons d'un element, com un paràgraf o altres tags que veurem més endavant es canvia amb la propietat background-color, per exemple:

```
<p style="color:blue;background-color: yellow">color de text blau i color de fons groc</p>
```

## Opacitat:

Es pot regular l'opacitat d'un element (o la seva transparència) de diferents formes:

- Utilitzant la propietat opacity, que va des de 0 (transparent) fins a 1 (opac).

Exemple: 

![image](https://user-images.githubusercontent.com/110727546/217008977-3a15475e-4ac6-48dc-80a6-d75b60f70c56.png)


- Utilitzant RGBA (Red Green Blue Alpha), en lloc de RGB.

Exemples: 50% de transparència.

```
style="background: rgb(0, 128, 0,0.5);"
```

![image](https://user-images.githubusercontent.com/110727546/217009682-8736fd7c-5ae0-45eb-b929-92a5a1d63df6.png)
