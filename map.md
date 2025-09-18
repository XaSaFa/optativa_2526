# HTML

## Mapes d'imatge:

Els mapes d'imatge són imatges dintre de les quals podem definir àrees clicables.

Les àrees són links a altres recursos web.

[Exemple W3Schools](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_map2)

Per a crear els mapes d'imatge primer hem de mostrar la imatge amb el tag img:

```
<img src="workplace.jpg" alt="Workplace" usemap="#workmap" width="400" height="379">
```

I definir el nom del mapa amb la paraula **usemap=#nom del mapa**.

A l'exemple es crea un mapa anomenat **workmap**.

Després generem les àrees del mapa:

```
<map name="workmap">
  <area shape="rect" coords="34,44,270,350" alt="Computer" href="computer.htm">
  <area shape="rect" coords="290,172,333,250" alt="Phone" href="phone.htm">
  <area shape="circle" coords="337,300,44" alt="Cup of coffee" href="coffee.htm">
</map>
```

A l'atribut name de map hem d'indicar el mateix nom anterior, a l'exemple **workmap**.

cada àrea clicable es defineix amb l'etiqueta area i s'indica la forma que tindrà: 

- rect: Rectangle.
- circle: Cercle.
- default: Tot el mapa.
- poly: Un polígon.

Per a rectangle s'han d'indicar les coordenades inicial i final en format de punt (x,y): 

![image](https://user-images.githubusercontent.com/110727546/214022823-cd5a0b13-0255-41a7-9eba-575769b25bda.png)

Resultat:

![image](https://user-images.githubusercontent.com/110727546/214022945-f6fec783-9046-4421-8b57-e123c6ff04f8.png)

Per al cercle s'indica el punt central del cercle i el seu radi:

![image](https://user-images.githubusercontent.com/110727546/214023059-db3d886b-cae8-4cb0-8a21-af65bcc4f9d4.png)

Resultat:

![image](https://user-images.githubusercontent.com/110727546/214023108-25211b26-2a7d-4ca8-b5b8-49185f5e0cd6.png)
