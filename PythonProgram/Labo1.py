#!/usr/bin/python3


letra = input("Letra:")

cantidad = input("Numero:")
Numero = int(cantidad)


for i in range (Numero):
    for j in range (i+1):
      print (letra, end="")

    print()
