#!/usr/bin/env python

__author__ = "Sebas Volpe"
__email__ = "compras@bari.com.ar"
__version__ = "1.00"

import json
import requests
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec

def fetch(data):
    filtrado = [x for x in data if x.get("currency_id") == "ARS"]
    return filtrado

def transform(dataset,min,max):
    minimo = [x for x in dataset if x.get("Price") < min]
    min_max = [x for x in dataset if (x.get("Price") > min and x.get("Price") < max)]
    maximo = [x for x in dataset if x.get("Price") > max]
    return [minimo,min_max,maximo]

def report(dataset, title=''):
    x = [data[0] for data in dataset]   
    y = [data[1] for data in dataset]
    z = [data[2] for data in dataset]

    

if __name__ == '__main__':

    url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Caba%20&limit=50"
    response = requests.get(url)

    # Cargo los datos necesarios
    ml = response.json()
    results = ml["results"]

    # Filtro solo los de Pesps
    pesos = fetch(results)

    # Filtro solo Precios, condicion...
    dataset = [
        {"Price":x.get("price"),
        "Condition":x.get("condition")
        } 
        for x in pesos
        ]

    trasn = transform(dataset,10000,110000)


    print(trasn["'Price"][1])
    #report(trasn,"titulo")


    



