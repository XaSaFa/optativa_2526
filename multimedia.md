# HTML

## Multimedia:

El terme multimedia es refereix a utilitzar múltiples entrades d'informació per les persones, com és l'audio, imatges o vídeo.

Els navegadors web al principi només soportaven text en un color, després van incloure text en colors, imatges, sons i vídeo.

Alguns els formats multimedia més coneguts:

### Formats de vídeo:

![image](https://user-images.githubusercontent.com/110727546/215461874-728bde49-211e-4583-b9f3-5c6eab868c4f.png)

![image](https://user-images.githubusercontent.com/110727546/215461923-9f1e8b89-af0b-406f-8e38-117ac9a8bbbf.png)

### Formats d'audio:

![image](https://user-images.githubusercontent.com/110727546/215462062-39f376cf-f62f-4617-aab8-6eee0fdb1840.png)

![image](https://user-images.githubusercontent.com/110727546/215462098-4c12775f-854b-4462-8636-899dd928b191.png)

## Vídeo: 

Serveix per mostrar un vídeo a una web, utilitza els tags video i source:

- video: Tag per contenir el vídeo, pot tenir els següents atributs:
  - controls: Mostra els botons per gestionar el vídeo.
  - autoplay: El vídeo s'inicia automàticament.
  - muted: El vídeo té el so al 0.
  - loop: Indica que el vídeo es mostrarà en bucle.
  - src: Indica la URL del vídeo, però això normalment s'indica al tag source.
- source: Indica la URL del vídeo. Pot haver més d'un tag source per cada vídeo, indicant fonts diferents per adaptar-se al navegador.

Exemple:

```
<video width="320" height="240" autoplay muted>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>
```

A l'exemple primer s'intentaria mostrar el vídeo mp4 i, en cas que no pogués el navegador provaria el ogg.

Si cap dels dos es pot mostrar escriuria la frase a la web: "Your browser does not support the video tag.".

[Vídeo](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_video_autoplay_mute)

## Audio:

Exactament igual que video però per a fitxers d'audio.

Exemple:

```
<audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
  Your browser does not support the audio tag.
</audio>
```

[audio](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_audio).

## Youtube:

Podem mostrar vídeos de Youtube al nostre web també. Per a fer-ho utilitzarem el tag iframe.

```
<iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY">
</iframe>
```

[Link exemple](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_youtubeiframe)

Un vídeo de Youtube normalment té un codi identificador de Youtube.

![image](https://user-images.githubusercontent.com/110727546/215465191-3c12d502-1174-4494-b656-d10d88c13593.png)

Aquest codi és el que necessitem per a la nostra web.

Per indicar opcions al navegador hem d'afegir-les al codi de youtube, per exemple, un vídeo amb autoplay, en bucle i sense so seria:

```
<iframe width="420" height="345" src="https://www.youtube.com/embed/X7YcjCkqrdA?autoplay=1&mute=1&loop=1">
</iframe>
```

Si volem amagar els controls ficaríem controls=0.

Aquest codi HTML també el podem obtenir anant al vídeo de Youtube i utilitzant l'opció compartir->insertar.

![image](https://user-images.githubusercontent.com/110727546/215465977-f3786869-3368-4e61-9f9e-81365ad9eb8d.png)

![image](https://user-images.githubusercontent.com/110727546/215466037-f988c974-ce37-4781-aa69-568967deec8e.png)

![image](https://user-images.githubusercontent.com/110727546/215466091-ff905f3b-3e23-4853-b282-4c5d0285ef08.png)







