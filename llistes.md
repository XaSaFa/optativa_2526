# HTML

## Llistes:

![image](https://user-images.githubusercontent.com/110727546/215451267-31855edb-152e-4b1c-9fe8-31ce67773d7e.png)


Les llistes serveixen per tenir una ordenació d'elements, com una llista de la compra.

Hi ha tres tipus de llistes: ordenades, desordenades i de definició.

### Llistes ordenades:

#### Tag ol (ordered list).

Aquestes llistes numeren cada element ja sigui amb números com lletres.

Exemple:

```
<ol>
  <li>Llet</li>
  <li>Pomes</li>
  <li>Pa</li>
</ol>
```

![image](https://user-images.githubusercontent.com/110727546/215452045-18bc4aa5-599f-4022-a2ba-85ddf76a2ac0.png)

Si no definim res la llista començarà per 1 i anirà incrementant el seu número per cada element fins l'últim.

Podem indicar a la llista que no comenci per 1 si no per un altre número, com per exemple el 10, amb l'atribut start:

```
<ol start="10">
  <li>Llet</li>
  <li>Pomes</li>
  <li>Pa</li>
</ol>
```

![image](https://user-images.githubusercontent.com/110727546/215452252-d55add40-7deb-49df-809d-77adf91e3181.png)

Si en lloc de números volem que la llista utilitzi lletres ho podem dir amb l'atribut type:

```
<ol type="a">
  <li>Llet</li>
  <li>Pomes</li>
  <li>Pa</li>
</ol>
```

![image](https://user-images.githubusercontent.com/110727546/215452660-474535cd-264c-4948-9f17-f695a603e3ab.png)

L'atribut type permet més variants:

- 1 números.
- A lletres majúscules.
- a lletres minúscules.
- I números romans majúscules.
- i números romans minúscules.

### Llista desordenada:

#### Tag ul (unordered list).

Aquestes llistes s'utilitzen quan l'ordre dels elements no importa, com a una llista de la compra.

Exemple:

```
<ul>
  <li>Llet</li>
  <li>Pomes</li>
  <li>Pa</li>
</ul>
```

![image](https://user-images.githubusercontent.com/110727546/215453951-359c8f64-a281-4b0d-852a-caac5f58f8ed.png)

Podem anidar llistes dins de llistes:

```
<ul>
  <li>Llet</li>
  <ul>
  	<li>Desnatada</li>
    <li>Semi</li>
  </ul>
  <li>Pomes</li>
  <li>Pa</li>
</ul>
```

![image](https://user-images.githubusercontent.com/110727546/215459046-7a7b1c47-d2e3-4962-b25d-cb9de03b2537.png)

Els atributs de les llistes desordenades es poden canviar mitjançant CSS.

També podem canviar l'atribut type per canviar la forma del indicador d'element entre: circle, disc, square o none.

Exemple:

```
<ul type="circle">  
 <li>HTML</li>  
 <li>Java</li>  
 <li>JavaScript</li>  
 <li>SQL</li>  
</ul>  
```

![image](https://user-images.githubusercontent.com/110727546/215499015-0b9a19ef-a753-4703-a997-b450ea9faf86.png)


### Llista de definició:

#### tag dl (description list).

Les llistes de definicions són llistes que serveixen per definir els seus elements.

Consten de 3 tags:

- dl: Llista de definició.
- dt: Paraula a descriure.
- dd: Descripció de la paraula.

Exemple:

```
<dl>
  <dt>IBM PC</dt>
  <dd>Ordinador de 1981 comercialitzat per IBM.</dd>
  <dt>Apple II</dt>
  <dd>Ordinador de 1977 comercialitzat per Apple.</dd>
</dl>
```

![image](https://user-images.githubusercontent.com/110727546/215460069-0bdfcf3d-1369-4a86-8f1b-2b3f58f4d7b1.png)

## Practicar:

[Fes aquests exercicis](https://www.w3schools.com/html/exercise.asp?filename=exercise_html_lists1)



