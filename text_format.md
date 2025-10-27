# CSS

## Formatejar text.

Formatejar text vol dir indicar el tamany, color, font, etc. d'un text.

### Alinear text:

#### text-align

El text el podem alinear dins de l'element on es trova de tres formes:
- A la dreta.
- A l'esquerra.
- Al centre.
- Justificat.

Per defecte un text estarà alineat a l'esquerra.

Exemple d'alineació al centre:

```
h1 {
  text-align: center;
}
```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_text-align).

#### text-align-last:

Aquesta propietat indica com s'ha d'alinear l'última línia d'un text.

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_text-align-last)

#### text-direction:

Aquesta propietat indica el sentit de lectura del text, els valors habituals són:
- ltr (esquerra a dreta, el normal).
- rtl (dreta a esquerra).

Anirà acompanyada de la propietat unicode-bidi.

Exemple:

```
p {
  direction: rtl;
  unicode-bidi: bidi-override;
}
```
[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_text_direction)

#### vertical-align:

Aquesta propietat permet definir l'alineament vertical del text envers de la resta d'elements.

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_vertical-align)

### Text Decoration:

Podem acompanyar el text de línies per sobre o per sota.

#### text-decoration-line:

Indica que volem acompanyar al text d'una línia de decoració, es poden convinar:
- overline (sobre el text).
- underline (sota el text).
- line-throught (text ratllat).
- none (cap).

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_text-decoration-line)

#### text-decoration-color:

Indica el color de les línies de decoració.

[Exemple web.](https://www.w3schools.com/css/css_text_decoration.asp)

#### text-decoration-style:

Estil de la línia de decoració, pot ser:

![image](https://user-images.githubusercontent.com/110727546/219400091-5dcba430-d2a0-496d-8048-aa472efec2b5.png)

[Exemple web.](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_text-decoration-style)

#### text-decoration-thickness:

Gruix de la línia de decoració.

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_text-decoration-thickness)

### Transformar text

#### text-transform:

Podem alterar el text per possar-lo en majúscules, minúscules, lletres inicials majúscules...

![image](https://user-images.githubusercontent.com/110727546/219403284-00f4041a-6ed6-490a-ae18-af249e8ee29d.png)

[Exemple web.](https://www.w3schools.com/css/tryit.asp?filename=trycss_text-transform)

### Espaiar el text

Podem controlar els espais del text que mostrem al web.

#### text-indent:

Serveix per sagnar el text 

```
p {
  text-indent: 50px;
}
```

![image](https://user-images.githubusercontent.com/110727546/219404384-4d189bbb-128a-40eb-b158-a49761b6f288.png)

#### letter-spacing:

Serveix per indicar la separació de les lletres.
- Si el número és positiu les lletres estaran més separades.
- Si el número és negatiu les lletres estaran més juntes.

 ```
 h2 {
  letter-spacing: 5px;
}
 ```
![image](https://user-images.githubusercontent.com/110727546/219405797-39bdb88d-5cd5-49aa-90c9-2c8adb80067d.png)

 ```
 h2 {
  letter-spacing: -2px;
}
 ```
![image](https://user-images.githubusercontent.com/110727546/219405631-5878942d-b98a-4357-ac52-f8089869f6d5.png)

#### line-height:

Indica la separació entre línies, la separació normal és 100% o 1:

```
p{
  line-height: 1;
}
```

![image](https://user-images.githubusercontent.com/110727546/219406853-38709f85-1ef5-414d-9b03-f7ca1b24f846.png)

Línies més juntes, valor inferior a 1:

```
p{
  line-height: 0.6;
}
```

![image](https://user-images.githubusercontent.com/110727546/219407069-ea9a4040-945c-4eaa-adbe-4ece98e3b00f.png)

Línies més separades, valor superior a 1:

```
p{
  line-height: 1.6;
}
```

![image](https://user-images.githubusercontent.com/110727546/219407190-d267c47a-95aa-476d-9f8d-3badeb92a48a.png)

#### text-shadow

Serveix per a fer una ombra darrera del text.

![image](https://user-images.githubusercontent.com/110727546/219408126-f2cfc4f0-4cbc-49b7-ab21-66566ceaf0c4.png)

Exemple d'ombra de color verd:

```
h1 {
  text-shadow: 2px 2px lime;
}
```

![image](https://user-images.githubusercontent.com/110727546/219407712-67b26ff4-8016-4f67-ba07-4472c287365c.png)

Exemple d'ombra de color vermell amb difuminat:

```
h1 {
  text-shadow: 2px 2px 5px red;
}
```

![image](https://user-images.githubusercontent.com/110727546/219408966-1e1d275b-45a4-4447-8f8f-bd64436d3049.png)

Exemple convinant dues ombres:

```
h1 {
  text-shadow: 0 0 3px lime, 0 0 5px red;
}
```

![image](https://user-images.githubusercontent.com/110727546/219409305-0d617230-9717-4525-aa77-17bde4305ce4.png)

## [Practicar](https://www.w3schools.com/css/exercise.asp?filename=exercise_text1)






