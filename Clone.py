# -*- coding: latin-1 -*-
import requests


def mostrar_menu():
  print("Bienvenido al menu:")
  print("1. Clonar")
  print("2. Salir")


def opcion_1():
  url = input("Por favor, introduce la URL a clonar: ")
  clonar_pagina(url)


def opcion_2():
  print("Saliendo del programa")


def clonar_pagina(url):
  try:
    datos = requests.get(url)
    if datos.status_code == 200:
      with open("index.html", "wb") as f:
        f.write(datos.content)
      print("Clonacion Exitosa")
    else:
      print("Error al clonar la pagina. Codigo de estado:", datos.status_code)
  except requests.RequestException as e:
    print("Error al conectar con la pagina:", e)


while True:
  mostrar_menu()
  opcion = input("Selecciona una opcion: ")

  if opcion == "1":
    opcion_1()
  elif opcion == "2":
    opcion_2()
    break
  else:
    print("Opcion invalida. Por favor, selecciona una opcion valida.")
