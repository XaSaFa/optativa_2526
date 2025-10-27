# CSS

![image](https://user-images.githubusercontent.com/110727546/218313563-f4f80669-f821-4111-ada8-e8e69882f67f.png)

## Margin

L'element margin serveix per crear un marge que envolta un element i que està per fora d'ell, de la seva vora (border).

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_margin_sides)

Els marges es poden definir indivialment per cada costat:

![image](https://user-images.githubusercontent.com/110727546/218313149-1d7c446b-f582-41dd-9ec0-48a016b4e74a.png)

O directament en una línia:

![image](https://user-images.githubusercontent.com/110727546/218313172-ccad21d1-dc5f-4208-8162-a0ed5719b05a.png)

- Si margin té 4 valors s'està indicant el valor individual de top, right, bottom left.
- Si margin té tres valors s'especifica el valor de top, (right i left), bottom.
- Si margn té dos valors s'especifica el valor de (top i bottom), (right i left).
- Si només té un valor serà el mateix valor pels quatre costats.

### Valor auto:

El valor auto serveix per centrar horitzontalment l'element dins del seu contenidor.

![image](https://user-images.githubusercontent.com/110727546/218313625-4453da7b-5d47-4ba8-91b5-fddf4977eb30.png)

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_margin_auto)

### Valor inherit:

Podem fer que els elements heretin el marge (tinguin el mateix) que els elements dins els quals estan, ho fem amb la paraula inherit

![image](https://user-images.githubusercontent.com/110727546/218313800-a2dda78c-80a0-4b34-8ace-c2985d8606db.png)

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_margin-left_inherit)

### Margin collapse:

Els marges de dalt i baix tenen la propietat collapse, la qual no afecta als marges d'esquerra i dreta.

Aquesta propietat fa que els marges top i bottom de dos elements que es toquen no es sumin si no que s'emplei el valor més alt dels dos.

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_margin_collapse)

![image](https://user-images.githubusercontent.com/110727546/218313997-e0ee33eb-650d-4311-ab8d-6052e65e9f93.png)

A l'exemple en lloc de tenir dos marges sumats de 10px, per un vaor de 20px només hi haurà un marge de 10px (el valor més alt).

### Practicar:

[Pràctica](https://www.w3schools.com/css/exercise.asp?filename=exercise_margin1).

## Padding:

El padding serveix per omplir espai dins d'un element fins a la seva vora, es com farcir un element.

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_padding_intro)

Igual que amb el margin podem especificar el padding per als quatre costats o amb tres valors, dos o un.

Especifiquem el padding individualment per cada costat:
![image](https://user-images.githubusercontent.com/110727546/218314311-6cc6c4a8-1185-4427-bde2-e418fd25f995.png)

Especifiquem el padding per cada costat pero a una sola línia:
![image](https://user-images.githubusercontent.com/110727546/218314326-dd073978-8ed5-4889-8b60-2e204301a9df.png)

Especifiquem el padding de top, (right i left) i bottom:
![image](https://user-images.githubusercontent.com/110727546/218314380-ad37bcab-7976-451e-908f-485f8a2d3546.png)

Especifiquem el padding de (top i bottom) i (right i left):
![image](https://user-images.githubusercontent.com/110727546/218314412-4df24ac6-d204-4aed-8c11-96c052623042.png)

Especifiquem el mateix padding pels quatre costats:
![image](https://user-images.githubusercontent.com/110727546/218314424-227ecced-a08c-46da-a510-dd7b0399c56f.png)

### Width:

L'amplada d'un element inclou el que ocupa l'element en si **MÉS** el padding, així que si volem que un element tingui una amplada determinada hem de vigilar amb el padding que té assignat.

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_padding_width)

![image](https://user-images.githubusercontent.com/110727546/218314498-d79a47cb-8ae1-41f1-85aa-7d7df1d1d78b.png)

Si es vol mantenir una amplada determinada sense que afecti el padding a cada element haurem d'utilitzar la propietat ```box-sizing: border-box;```

[Exemple web](https://www.w3schools.com/css/tryit.asp?filename=trycss_padding_width2)

![image](https://user-images.githubusercontent.com/110727546/218314570-070cf2ab-0d63-4433-b723-19c777961e88.png)

### Practicar:

[Pràctica](https://www.w3schools.com/css/exercise.asp?filename=exercise_padding1).
