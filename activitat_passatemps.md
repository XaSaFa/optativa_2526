# Passatemps

En aquesta activitat faràs una pàgina web de passatemps utilitzant HTML i **CSS INTERN**.

Per canviar el tamany de la font del text heu de fer servir la propietat CSS font-size, per exemple ```font-size:40px;```.

La web tindrà els següents apartats:

- Capçalera amb el títol "Passatemps de X", on X és el teu cognom.
- Un Sudoku de números com el de l'exemple.
  - Canvieu els colors per els de la vostra elecció.
  - Mireu que hi ha cel·les que són de diferent tamany.
- Un Sudoku amb imatges (per pujar nota), igual que la imatge adjunta de Sudoku de fruites, però canviant les imatges per unes de la vostra elecció.
  - Estarà fet utilitzant una taula i les propietats CSS que considereu necessàries.

Entregueu la pàgina web juntament amb les imatges i el fitxer css a Moodle.

# Exemples

## Sudoku de fruites:

<img width="325" height="330" alt="image" src="https://github.com/user-attachments/assets/4f6e5303-8e98-4ff8-a513-12ea22bb552f" />

## Sudoku de números:

<img width="464" height="462" alt="image" src="https://github.com/user-attachments/assets/d8d132d4-7524-49b3-b4d2-ff92eb51cdcf" />

## Exemple sudoku petit:

<img width="380" height="410" alt="image" src="https://github.com/user-attachments/assets/b31fa5d8-ba42-4039-889f-52cb42608300" />


```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        
        table, td{
            border-collapse: collapse;
            border: 1px solid black;
        }
        td{
            padding: 20px 30px;
            font-size:40px;
        }
        .cela-lila{
            background-color: rgb(216, 165, 201);
        }
        .dreta_gruixut{
            border-right-width: 4px;
        }
        .sota_gruixut{
            border-bottom-width: 4px;
        }
    </style>
</head>
<body>
    <table>
        <tr><td class="cela-lila dreta_gruixut sota_gruixut">8</td><td class="sota_gruixut">6</td></tr>
        <tr><td class="dreta_gruixut">1</td><td></td></tr>
    </table>
</body>
</html>
```
