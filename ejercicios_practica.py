#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.axes


def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    datos = {
                  "nombre": "Sebas",
                  "apellido": "Volpe",
                  "dni": "2411545",
                  "ropas": [
                      {"prenda": "zapatilla", "cantidad": 4},
                      {"prenda": "remeras", "cantidad": 12},
                      ]
            }
    with open('datos.json', 'w') as jsonfile:
        data = [datos]
        json.dump(data, jsonfile, indent=4)


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1

    with open('datos.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    
    with open('prueba.xml', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(json.dumps(data, indent=4))


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.

    
    root = ET.Element("XML")
    ET.SubElement(root,"Nombre").text = "Sebastian"
    ET.SubElement(root,"Apellido").text = "Volpe"
    ET.SubElement(root,"Dni").text = "24112054"
    ET.SubElement(root,"zapatilla").text = "4"
    ET.SubElement(root,"remeras").text = "12"


    a = ET.ElementTree(root)

    a.write("prueba.xml")
      



def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.

    tree = ET.parse('prueba.xml')
    root = tree.getroot()

    print('Recorrer el archivo XML')
    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)


def ej5():
    # Ejercicio de consumo de datos por API
    
    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()
                    

    id_1 = [1 for x in data if (x['userId'] == 1) and (x['completed'] == True)]
    id_2 = [1 for x in data if (x['userId'] == 2) and (x['completed'] == True)]
    id_3 = [1 for x in data if (x['userId'] == 3) and (x['completed'] == True)]
    id_4 = [1 for x in data if (x['userId'] == 4) and (x['completed'] == True)]
    id_5 = [1 for x in data if (x['userId'] == 5) and (x['completed'] == True)]
    id_6 = [1 for x in data if (x['userId'] == 6) and (x['completed'] == True)]
    id_7 = [1 for x in data if (x['userId'] == 7) and (x['completed'] == True)]
    id_8 = [1 for x in data if (x['userId'] == 8) and (x['completed'] == True)]
    id_9 = [1 for x in data if (x['userId'] == 9) and (x['completed'] == True)]
    id_10 = [1 for x in data if (x['userId'] == 10) and (x['completed'] == True)]

    completadas = [len(id_1),len(id_2),len(id_3),len(id_4),len(id_5),len(id_6),len(id_7),len(id_8),len(id_9),len(id_10)]


    labels = [
        'user1', 'user2', 'user3', 'user4', 'user5',
        'user6', 'user7','user8', 'user9', 'user10' ]

    fig, ax = plt.subplots()
    fig.suptitle('Aprobadas por usuario')

    ax.pie(completadas, labels = labels, autopct='%1.1f%%', startangle=180)
    ax.axis('equal') 

    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    #ej3()
    # ej4()
    ej5()
