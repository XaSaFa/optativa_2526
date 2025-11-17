```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* Fes una taula de dues files i dues columnes 
        -----
        |A|B|
        -----
        |C|D|
        -----
        -Cada Cel·la té un color de fons diferent.
        -Cada cel·la té un color de vores diferents.
        -Les vores interiors són de color groc.
        -Els elements estan separats 20px de la vora.*/
        td,table{
            border-collapse: collapse;
            border: 3px black solid;
        }
        td{
            padding: 20px;
        }

        
        .cel1{
            background-color: aquamarine;
            border-color: lime;

        }
        .cel2{
            background-color: blueviolet;
            border-color: firebrick;
        }
        .cel3{
            background-color: magenta;
            border-color: cornflowerblue;

        }
        .cel4{
            background-color: darkcyan;
            border-color: sandybrown;
        }
        
        .groc_dreta{
            border-right-color: yellow;
        }
        .groc_sota{
            border-bottom-color: yellow;
        }
        
    </style>
</head>
<body>
    
    <table>
        <tr>
            <td class="cel1 groc_dreta groc_sota">A</td>
            <td class="cel2 groc_sota">B</td>
        </tr>
        <tr>
            <td class="cel3 groc_dreta">C</td>
            <td class="cel4">D</td>
        </tr>
    </table>
</body>
</html>
```
