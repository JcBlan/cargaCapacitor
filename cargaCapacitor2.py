
# Ejercicio 2

import math
import json
import matplotlib.pyplot as plt
from cargaCapacitor1 import minimosCuadrados


def regresionLineal(coeficientes, x):
    return coeficientes[0] + (coeficientes[1] * x)


# Cargar datos desde json
with open("datos.json", "r") as datos:
    valores = json.load(datos)
datos.close()

#convertir dict a list
valoresX = []
valoresY = []

#convertir string a float
for x, y in valores.items():
    valoresX.append(float(x))
    valoresY.append(float(y))

# plot valores experimentales
plt.plot(valoresX, valoresY, "bo")
plt.axis([0, max(valoresX), 0, max(valoresY)])
plt.show()

# coeficientes de regresion = (a0, a1)
coeficientes = minimosCuadrados("datos.json")

valoresLinealY = []
#hallar incognitas de la regresion  
for x in valoresX:
    valoresLinealY.append(regresionLineal(coeficientes, x))

# Calcular error estandar
Sr = 0
for i in range(0, len(valoresX)):
    Sr = Sr + math.pow( (valoresLinealY[i] - coeficientes[0] -  (coeficientes[1] * valoresX[i] ) ), 2)

# error estándar del estimado
Syx = math.sqrt( Sr / (len(valoresX)-2 ))
print("\nError estandar del Estimado: ", Syx)



