
#Crear el juego del ahorcado?
#Si!!

import random

figuras_ahorcado = [ """

   +-----+
         |
         |
         |
         |
________________""","""
   +-----+
         |
   O     |
         |
         |
________________""","""
   +-----+
         |
   O     |
   |     |
         |
________________""","""
   +-----+
         |
   O     |
  /|\    |
         |
________________""","""
   +-----+
         |
   O     |
  /|\    |
    \    |
________________""","""
   +-----+
         |
   O     |
  /|\    |
  / \    |
________________""","""
   +-----+
   |     |
   Ô     |
  /|\    |
  / \    |
________________"""]


palabras = ['mesa','silla','hipopotamo','lampara','armario','gorro','botella','perro']


caracter = ""
palabra_adivinar = random.choice(palabras)
palabra_adivinar = palabra_adivinar.upper()
palabra = "-" * len(palabra_adivinar)
figura = ""
indice = 0


print("La palabra tiene", len(palabra_adivinar), "letras")
print("")


pista = input("Te gustaria una pista? S/N: ")
print("")
pista = pista.upper()

if pista == "S":
  print("La palabra comienza por '" + palabra_adivinar[0] + "'")

while caracter != "SALIR" and figura != figuras_ahorcado[len(figuras_ahorcado) -1] and palabra != palabra_adivinar:
  
  print("")
  print(palabra)
  print("")

  caracter = input("Introduce una letra: ")
  caracter = caracter.upper()
  contador = 0
  for letra in palabra_adivinar:
    if letra == caracter:
      palabra = palabra[:contador] + letra + palabra[contador + 1:]
    contador += 1
  if caracter not in palabra_adivinar:
    figura = figuras_ahorcado[indice]
    indice += 1
  print(figura)
 


if figura == figuras_ahorcado[len(figuras_ahorcado) - 1]:
  print("Perdiste! La palabra era: ", palabra_adivinar)
elif palabra == palabra_adivinar:
  print(palabra)
  print("Super! Adivinaste quieres volver a jugar??:")
else:
  print("Has salido del juego")