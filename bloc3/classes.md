# Classes

Les classes serveixen per organitzar la informació i funcions d'un programa informàtic de forma lògica.

Gràcies a les classes el nostre codi serà més fàcil d'entendre, utilitzar, mantenir i debugejar (corregir errors).

## Classes i objectes

Una classe és una plantilla per a organitzar la informació i un objecte és una instància d'una plantilla, la materialització de la plantilla.

<img width="800" height="400" alt="imatge" src="https://github.com/user-attachments/assets/503e75b2-d591-41c2-8d35-930ae0d51547" />

## Estructura d'una classe

Les classes es declaren amb la paraula reservada **class** seguida del nom de la classe.

Les classes tenen una funció d'inicialització anomenada __init__ que serveix per passar els valors dels atributs a l'objecte creat.

```
# Classe persona amb els seus atributs i funcions
class Persona:

    # Funció d'inicialització, aquí li passem els atributs
    def __init__ (self, nom, cognom1, cognom2, dni):        
        self.nom = nom
        self.cognom1 = cognom1
        self.cognom2 = cognom2        
        self.dni = dni
```

## Creació d'un objecte Persona

Aquesta classe Persona té una funció d'inicialització que rep els valors dels atributs: nom, cognom1, cognom2 i dni.

Vaig a crear dos objectes de la classe Persona.

```
manel = Persona("Manel", "Sanchez", "Rubiales", "56765432T")
lola = Persona("Lola", "Prats", "Celma", "34256541V")
```

## Atributs dels objectes

Per accedir a un atribut d'un objecte es fa servir el nom de l'objecte seguit de punt i el nom de l'atribut. Per exemple, per comprobar si s'han creat bé els objectes persona puc imprimir atributs dels objectes.

```
print (manel.nom)
print (lola.dni)
```
<img width="1012" height="752" alt="imatge" src="https://github.com/user-attachments/assets/07983f7f-2a11-415a-9c78-ea81d44eb9c0" />

## Funcions dins una classe

Normalment les classes tenen funcions per facilitar la feina dels programes que les utilitzen, per exemple puc crear la classe nom_sencer dins de la classe Persona que retorna una concatenació de nom i els dos cognoms d'una persona.

```
# Classe persona amb els seus atributs i funcions
class Persona:

    # Funció d'inicialització, aquí li passem els atributs
    def __init__ (self, nom, cognom1, cognom2, dni):
        self.nom = nom
        self.cognom1 = cognom1
        self.cognom2 = cognom2
        self.dni = dni

    # Funció que retorna la concatenació de nom, cognom1 i cognom2
    def nom_sencer (self):
        return (self.nom + " " +  self.cognom1 + " " + self.cognom2)
```

I la crido des del meu programa.

```
print(manel.nom_sencer())
```

<img width="1012" height="752" alt="imatge" src="https://github.com/user-attachments/assets/e46b7ace-14f6-4336-974d-1fc4e1b688e6" />

## Recursos

- [Apunts de Classes a W3Schools](https://www.w3schools.com/python/python_oop.asp)
