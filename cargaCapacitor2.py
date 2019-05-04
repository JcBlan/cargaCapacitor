
# Ejercicio 2

import json
import matplotlib.pyplot as plt

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


