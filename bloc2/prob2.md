# Problemes de variables amb input

Per tal de fer aquests problemes utilitzarem la funció de Python input, que demana una entrada d'informació per teclat a l'usuari

Exemple 1:

```
nom_usuari = input("Introdueix el teu nom: ")
print("Hola "+ nom_usuari)
```

Demana a l'usuari el seu nom i el guarda dins la variable nom_usuari, després imprimeix per pantalla el missatge Hola seguit del nom introduit per l'usuari.

Exemple 2:

```
num1 = 10
num2 = input("Introdueix el número que vols multiplicar per 10: ")
print(num1 * int(num2))
```

Pregunta un número a l'usuari i mostra per pantalla el resultat de multiplicar aquell número per 10 (veieu que es fa un casting per que la variable introduida per l'usuari sigui un número en lloc de text).

1. Demana a l’usuari el seu nom i mostra un missatge de benvinguda.
2. Demana dos números enters a l’usuari i mostra’n la suma.
3. Demana a l’usuari la seva edat i calcula en quin any va néixer.
4. Demana un número decimal i mostra’l arrodonit amb round().
5. Demana a l’usuari una temperatura en graus Celsius i converteix-la a Fahrenheit.
6. Demana el preu d’un producte i el percentatge d’impost, i calcula el preu final.
7. Demana dos costats d’un rectangle i mostra’n l’àrea.
8. Demana el color preferit de l’usuari i mostra un missatge que el contingui.
9. Demana el radi d’un cercle i calcula la seva àrea.
10. Demana a l’usuari dues paraules i concatena-les separades per un espai.
