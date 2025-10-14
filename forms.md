# HTML

## Formularis

![image](https://user-images.githubusercontent.com/110727546/231860634-a185bcdb-298a-4b68-bc53-74bd7029c412.png)

Una de les coses més importants de cara a la web interactiva és que l'usuari/a pugui interactuar amb la nostra web, una de les maneres de fer-ho és mitjançant formularis.

Els formularis serveixen per rebre informació dels usuaris.

Els formularis utilitzen l'etiqueta FORM:

```
<form>

form elements

</form>
```

Una vegada que hem creat l'etiqueta dins el nostre HTML podem afegir diferents elements.

## Elements de formulari

Els elements que podem incloure dins del formulari són molt variats, tots ells serveixen per passar valors a la nostra aplicació.

Els valors es passen associats a una cosa anomenada **variable**.

Les variables són contenidors de valors identificats amb un nom, es diuen variables perquè el valor del contenidor pot variar.

![image](https://user-images.githubusercontent.com/110727546/231860539-414d9265-0a2a-4590-815c-8bc875577b3d.png)

El nom de cada variable és un atribut anomenat name.

![image](https://user-images.githubusercontent.com/110727546/231861459-9e07f4e8-ac1b-414a-98c2-aa8d1f459eea.png)

Els elements del formulari tenen una etiqueta pròpia anomenada input que pot ser de molts tipus diferents.

![image](https://user-images.githubusercontent.com/110727546/231860911-a8862c16-ca4b-4ca3-9ee1-5aa42e9b5872.png)

Veurem alguns dels més comuns a continuació.

### ⋆ text ⋆

És un requadre que serveix per escriure text.

![image](https://user-images.githubusercontent.com/110727546/231859620-7c394150-5940-4e39-b446-e06337798c42.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_text)

### ⋆ password ⋆

És un requadre de text on no es veu el text introduït.

![image](https://user-images.githubusercontent.com/110727546/231861622-143dd035-dbe5-477c-b189-d410f932f553.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_password)

### ⋆ radio ⋆

Es tracta d'un conjunt d'elements entre els quals només es pot seleccionar una opció

![image](https://user-images.githubusercontent.com/110727546/231862392-0e9d4bc9-bad0-4e9f-af11-b125a82d9697.png)

És important que tots els elements radio tinguin el mateix valor a l'atribut name.

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_radio)

### ⋆ checkbox ⋆

Es tracta d'un requadre que té dos possibles valors: activat o desactivat.

![image](https://user-images.githubusercontent.com/110727546/232056799-71562d8b-38fc-4341-af08-6284d95bdee3.png)

Quan un checkbox està actiu passa la variable "name" amb el seu valor "value".

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_checkbox2)

### ⋆ list ⋆

List permet escollir un valors d'entre una llista.

![image](https://user-images.githubusercontent.com/110727546/232077104-3a369e18-2487-4361-b229-92448f8e078d.png)

Cada valor posible estarà dins d'un element de tipus option:

```
<input list="browsers" name="browser">
  <datalist id="browsers">
    <option value="Internet Explorer">
    <option value="Firefox">
    <option value="Chrome">
    <option value="Opera">
    <option value="Safari">
  </datalist>
```

[Exemple web.](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_datalist)


### ⋆ color ⋆

Serveix per escollir un color.

![image](https://user-images.githubusercontent.com/110727546/232057865-a317747d-1af1-42c9-9e23-c2efd13bef14.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_color)

### ⋆ date ⋆

Serveixen per seleccionar una data.

![image](https://user-images.githubusercontent.com/110727546/232058023-2d3d457b-2b59-4466-8738-afeca88e1549.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_date)

Podem indicar que hi ha una data mínima i/o màxima entre les possibles opcions.

![image](https://user-images.githubusercontent.com/110727546/232058285-e6931af1-1f35-4a13-973c-a5c6592e2ce2.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_date_max_min)

### ⋆ time ⋆

Serveix per introduir una hora.

![image](https://user-images.githubusercontent.com/110727546/232063480-e02fa77f-d333-4e00-b0b2-5ec06fdd2c5c.png)

[Exemple web.](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_time)

### ⋆ datetime-local ⋆

Permet introduir data i hora.

![image](https://user-images.githubusercontent.com/110727546/232059463-b429204e-681f-47af-86da-4debb4f6720e.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_datetime-local)

### ⋆ email ⋆

Permet introduir un mail, fa una mínima comprovació del text introduït.

![image](https://user-images.githubusercontent.com/110727546/232059941-0157ab0b-b5da-49d9-b6e0-98f3953b4730.png)
![image](https://user-images.githubusercontent.com/110727546/232059995-4313998c-8a1c-4d65-9fe4-b272a2ffbc2b.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_email)

### ⋆ file ⋆

Permet seleccionar un fitxer de l'equip (normalment per pujar-lo a una aplicació).

![image](https://user-images.githubusercontent.com/110727546/232060507-c4fce8f3-0d52-4346-a9ef-a8e7e0ded954.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_file)

### ⋆ number ⋆

Permet introduir números en un requadre.

![image](https://user-images.githubusercontent.com/110727546/232061140-ffd00d7f-3263-485a-a979-56e99bde56da.png)

Pot tenir un valor mínim i màxim de forma opcional.

[Exemple web.](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_number)

### ⋆ range ⋆

Permet escollir un número d'entre un rang de valors.

![image](https://user-images.githubusercontent.com/110727546/232062101-1e3da18f-0be9-4fd8-bf9a-ad4d9fa6cee5.png)

[Exemple web.](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_range)

### ⋆ tel ⋆

És un requadre on es poden introduir números en el format especificat.

![image](https://user-images.githubusercontent.com/110727546/232062889-b80d7ec4-95a8-4d18-a46f-1b230cd8ac07.png)

[Exemple web.](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_tel)

### ⋆ button ⋆

Es tracta d'un botó.

![image](https://user-images.githubusercontent.com/110727546/232057647-1e4907f9-f48d-40de-9ed4-946f64fa9772.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_button)

### ⋆ reset ⋆ 

És un botó que esborra tot el que s'ha introduït a un formulari.

![image](https://user-images.githubusercontent.com/110727546/231862080-20a85481-f82f-460e-89b4-fd81d63d28ac.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_reset)

### ⋆ submit ⋆

És un botó que envia els valors introduïts al formulari a un destí, com per exemple una pàgina PHP.

![image](https://user-images.githubusercontent.com/110727546/231862080-20a85481-f82f-460e-89b4-fd81d63d28ac.png)

[Exemple web](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_reset)

## ⋆ textarea ⋆

L'element textarea és un requadre de text gran que permet introduir textos llargs.

![image](https://user-images.githubusercontent.com/110727546/232080401-50f2d119-6ab1-4405-8b3f-675f274b4d18.png)

S'indiquen les files (rows) i columnes (cols).

```
<textarea id="text" name="text" rows="4" cols="50"></textarea>
```

[Exemple web.](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_textarea)


## ⋆ Practicar ⋆ 

[Exercicis web.](https://www.w3schools.com/html/exercise.asp?filename=exercise_html_form_input_types1)
